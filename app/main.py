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


class InputData(BaseModel):
    question: str = Field(
        default=None, title="The question posted by the user"
    )
    details: str = Field(
        default=None, title="The associated data from the user's account"
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


@app.middleware("http")
async def cognito_authenticate(request: Request, call_next):
    try:
        token = request.headers["Authorization"]
    except KeyError:
        # return HTTPException(status_code=401)
        return JSONResponse(status_code=401, content="Authentication missing")  # or 401

    verification_of_token = cognito_validate(token)
    if verification_of_token:
        response = await call_next(request)
        return response
    else:
        return JSONResponse(status_code=401, content="Authentication failed")  # or 401


@app.get("/")
async def root():
    return {"message": "It's working"}


@app.post("/question")
def question(input_data: InputData):
    question = input_data.question
    details = input_data.details
    if not question and not details:
        return {"Please provide the question and details"}
    classified_list = openai_helper.classify_question(question)
    return classified_list
    if isinstance(classified_list, list): 
        if 'None' in classified_list:
            return {"message": "Invalid question"}
        classified_list = openai_helper.fetch_context(classified_list, question, "customer")
    else:
        return {"message": "It's working"}


if __name__ == '__main__':
    uvicorn.run("api:app", host="0.0.0.0", port=8080, reload=True)
