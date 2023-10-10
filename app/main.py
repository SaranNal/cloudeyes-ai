from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
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


class InputData(BaseModel):
    question: str = Field(
        default=None, title="The question posted by the user"
    ),
    customer_id: str = Field(
        default=None, title="The associated data from the user's account"
    )
    chat_id: str = Field(
        default=None, title="Chat thread id"
    ),
    account_id: str = Field(
        default=None, title="Customer account id"
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
def question(input_data: InputData):
    question = input_data.question
    customer_id = input_data.customer_id
    chat_id = input_data.chat_id
    account_id = input_data.account_id
    
    if not question:
        return {"Please pass a question"}
    classified_list = openai_helper.classify_question(question)
    
    if isinstance(classified_list, list): 
        if 'None' in classified_list:
            return {"message": "Invalid question"}
        openai_answer = openai_helper.openai_answer(classified_list, question, customer_id, chat_id)
        return openai_answer
    else:
        return {"message": "It's working"}


if __name__ == '__main__':
    uvicorn.run("api:app", host="0.0.0.0", port=8080, reload=True)


@app.get("/test")
def rtdd():
    customer_db = db_utility.get_database("dde7e592-80a0-420a-ad82-df2dd6b6322b")
    # customer_db.create_collection("chat_threads")
    collections = customer_db.list_collection_names()
    print(collections)
    return collections
