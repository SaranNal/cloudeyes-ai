from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException, Depends
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
from datetime import datetime
import itertools


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


async def get_api_key(api_key_header: str=Security(api_key_header)):
    if api_key_header == get_settings("api_key"):
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )

# @app.middleware("http")
# async def cognito_authenticate(request: Request, call_next):
#     try:
#         token = request.headers["Authorization"]
#     except KeyError:
#         # return HTTPException(status_code=401)
#         return JSONResponse(status_code=401, content="Authentication missing")  # or 401

#     verification_of_token = cognito_validate(token)
#     if verification_of_token:
#         response = await call_next(request)
#         return response
#     else:
#         return JSONResponse(status_code=401, content="Authentication failed")  # or 401


@app.get("/")
async def root():
    return {"message": "It's working"}


@app.post("/chat")
def question(input_data: QuestionData):
    question = input_data.question
    customer_id = input_data.customer_id
    chat_id = input_data.chat_id
    account_id = input_data.account_id
    openai_answer = []

    if not question:
        return {"Please pass a question"}
    classified_list = openai_helper.classify_question(question)

    if chat_id == "":
        chat_id = helper.generate_chatid(account_id)

    print("Chat thread id:", chat_id)

    message = "Please rephrase your question or ask a relevant question!"
    try:
        if isinstance(classified_list, list):
            if 'None' in classified_list:
                return {"answer": "Invalid question", "thread_id": "", "categories": [""]}
            answer = openai_helper.openai_answer(
                        classified_list, question, customer_id, account_id, chat_id)
            message, chat_reply = itertools.tee(answer)
            tasks = BackgroundTasks()
            print("appending chat")
            tasks.add_task(openai_helper.saving_chat, chat_reply, customer_id,
                        account_id, chat_id, question)
            return StreamingResponse(message, media_type="text/event-stream", background=tasks)
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
    chat_threads = chat_threads_collection.find({"account_id": account_id})

    response = {}
    for chat_thread in chat_threads:
        response[chat_thread["chat_id"]] = helper.summarize_string(
            chat_thread["chat_data"]["question"])

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

    response = {}
    for chat_thread in chat_threads:
        print(chat_thread)
        response[str(chat_thread["_id"])] = chat_thread["chat_data"]

    return response


if __name__ == '__main__':
    uvicorn.run("api:app", host="0.0.0.0", port=8080, reload=True)
