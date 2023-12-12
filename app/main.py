from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException, Depends
import pandas as pd
from starlette.status import HTTP_403_FORBIDDEN
from pydantic import BaseModel, Field, Json
from typing import Any
import app.helper as helper
import uvicorn
import app.openai_helper as openai_helper
import os
from app.authenticator.cognito import cognito_validate
from starlette.responses import JSONResponse
import app.db_utility as db_utility
from datetime import datetime, timedelta
import itertools
import json
import time
from app.db_utility import get_database


class QuestionData(BaseModel):
    question: str = Field(
        default=None, title="The question posted by the user"
    )
    customer_id: str = Field(
        default=None, title="The associated data from the user's account"
    )
    chat_id: str = Field(
        default=None, title="Chat thread id"
    )
    account_id: str = Field(
        default=None, title="Customer account id"
    )


class HistoryList(BaseModel):
    customer_id: str = Field(
        default=None, title="The associated data from the user's account"
    )
    account_id: str = Field(
        default=None, title="Customer account id"
    )


class HistoryItem(BaseModel):
    customer_id: str = Field(
        default=None, title="The associated data from the user's account"
    )
    account_id: str = Field(
        default=None, title="Customer account id"
    )
    chat_id: str = Field(
        default=None, title="Chat id"
    )


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
api_key_header = APIKeyHeader(name="access_token", auto_error=False)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == get_settings("api_key"):
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )


@app.middleware("http")
async def cognito_authenticate(request: Request, call_next):
    # since authorization isn't part of the OPTIONS request
    if request.method == "OPTIONS" or request.url.path in ['/', '/docs', '/favicon.ico', '/openapi.json']:
        response = await call_next(request)
        return response
    try:
        token = request.headers["Authorization"]
    except KeyError:
        return JSONResponse(status_code=401, content="Authentication missing")

    verification_of_token = cognito_validate(token)
    if verification_of_token:
        response = await call_next(request)
        return response
    else:
        return JSONResponse(status_code=401, content="Authentication failed")


@app.get("/")
async def root():
    return {"message": "It's working"}


def question_limiter(func):
    def decorator(input_data: QuestionData):
        customer_id = input_data.customer_id
        admin_db = get_database('admin')
        today = datetime.today()
        month_year = today.strftime("%b-%Y")
        customer_data = dict(admin_db['customers'].find_one(
            {'customer_id': customer_id}))
        if 'usage' in customer_data:
            if month_year in customer_data['usage']:
                if customer_data['usage'][month_year] > 100:
                    return {"message": "Limit exceeded"}
                customer_data['usage'][month_year] += 1
            else:
                customer_data['usage'][month_year] = 1
        else:
            customer_data['usage'][month_year] = 1
            filter_criteria = {"customer_id": customer_id}
            to_update_data = {"$set": {"usage": customer_data['usage']}}
            admin_db['customers'].update_one(filter_criteria, to_update_data)
        return func(input_data)
    return decorator


@app.post("/chat")
def question(input_data: QuestionData):
    question = input_data.question
    customer_id = input_data.customer_id
    chat_id = input_data.chat_id
    account_id = input_data.account_id
    if not question:
        return {"Please pass a question"}
    classified_list = openai_helper.classify_question(question)

    if chat_id == "":
        chat_id = helper.generate_chatid(account_id, question)

    print("Chat thread id:", chat_id)

    message = "Please rephrase your question or ask a relevant question!"
    try:
        if isinstance(classified_list, list):
            if 'None' in classified_list and chat_id == "":
                return {"answer": "Invalid question", "thread_id": "", "categories": [""]}
            elif 'None' in classified_list:
                classified_list = ["Utilization"]
            answer = openai_helper.openai_answer(
                classified_list, question, customer_id, account_id, chat_id)
            message, chat_reply = itertools.tee(answer)
            tasks = BackgroundTasks()
            print("appending chat")
            header = {
                "X-classification": json.dumps(classified_list),
                "X-chat-id": chat_id,
                "Cache-Control": "no-cache",
                "Connection": "keep-alive"
            }
            tasks.add_task(openai_helper.saving_chat, chat_reply, customer_id,
                           account_id, chat_id, question)
            return StreamingResponse(message, media_type="text/event-stream", background=tasks, headers=header)
        else:
            return {"answer": "Invalid question", "thread_id": "", "categories": [""]}

    except KeyError:
        print("OpenAI response is in unexpected format")


@app.post("/chat_history")
def list_chat_history(input_data: HistoryList):
    customer_id = input_data.customer_id
    account_id = input_data.account_id

    customer_db = db_utility.get_database(customer_id)
    chat_threads_collection = customer_db["chat_threads"]
    # group by chat_id, sort by timestamp desc and get one record
    chat_threads = chat_threads_collection.aggregate([
        {'$match': {'account_id': account_id}},
        {'$sort': {'timestamp': 1}},
        {
            '$group': {
                '_id': '$chat_id',
                'timestamp': {'$last': '$timestamp'},
                'chat_data': {'$push': '$chat_data'}
            }
        },
        {'$sort': {'timestamp': -1}},
        {
            "$project": {
                "_id": 0,
                "chat_id": "$_id",
                "timestamp": 1,
                "chat_data": 1
            }
        }
    ])

    response = []
    try:
        modified_chat_threads = []
        for chat_thread in chat_threads:
            chat_thread['chat_data'] = helper.summarize_string(
                chat_thread['chat_data'][0][0]['content'])
            modified_chat_threads.append(chat_thread)

        # Convert to DataFrame and set timestamp as index
        df = pd.DataFrame(modified_chat_threads)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)

        # Define date ranges
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        last_week = today - timedelta(days=7)
        last_month = today - timedelta(days=30)

        # Filter data for today, last week, and last month
        today_data = df[df.index.date == today.date()].transpose()
        last_week_data = df[(df.index.date > last_week.date()) & (
            df.index.date < today.date())].transpose()
        last_month_data = df[(df.index.date > last_month.date()) & (
            df.index.date < last_week.date())].transpose()
        # setup response in the desired format
        response = [
            {
                'date': "Today",
                'history': today_data
            },
            {
                'date': "Last Week",
                'history': last_week_data
            },
            {
                'date': "Previous 30 days",
                'history': last_month_data
            }
        ]

    except Exception as err:
        print('Unable to generate chat history', err)

    return response


@app.post("/chat_item")
def chat_item(input_data: HistoryItem):
    customer_id = input_data.customer_id
    account_id = input_data.account_id
    chat_id = input_data.chat_id

    customer_db = db_utility.get_database(customer_id)
    chat_threads_collection = customer_db["chat_threads"]
    chat_threads = chat_threads_collection.find(
        {"account_id": account_id, "chat_id": chat_id})

    response = []
    for chat_thread in chat_threads:
        chat_item = {}
        chat_data = chat_thread['chat_data']
        chat_item['question'] = chat_data[0]['content']
        chat_item['answer'] = chat_data[1]['content']
        response.append(chat_item)

    return response


if __name__ == '__main__':
    uvicorn.run("api:app", host="0.0.0.0", port=8080, reload=True)


@app.post("/stream-test")
def stream_test():
    return StreamingResponse(stream_gen(), media_type="text/event-stream")


def stream_gen():
    message = "lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quaerat."
    for word in message.split(" "):
        time.sleep(0.1)
        yield "data: " + word + "\n\n"
