from fastapi import FastAPI
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


async def get_api_key(api_key_header: str = Security(api_key_header)):
    """Validate the API key in the header"""
    if api_key_header == get_settings("api_key"):
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )


@app.get("/")
async def root():
    return {"message": "It's working"}


@app.post("/question")
def question(input_data: InputData):
    question = input_data.question
    details = input_data.details
    if not question and not details:
        return {"Please provide the question and details"}
    return openai_helper.classify_question(question)
    os._exit()
    return {
        "question": question,
        "details": details
    }

if __name__ == '__main__':
    uvicorn.run("api:app", host="0.0.0.0", port=8080, reload=True)
# testing the branch new
