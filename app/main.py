from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException, Depends
from starlette.status import HTTP_403_FORBIDDEN
from pydantic import BaseModel, Field, Json
from typing import Any
from .helper import get_answer, get_settings
import uvicorn


class Item(BaseModel):
    question: str = Field(
        default=None, title="The question posted by the user"
    )
    details: Json[Any] = Field(
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


settings = get_settings()
api_key_header = APIKeyHeader(name="access_token", auto_error=False)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    """Validate the API key in the header"""
    if api_key_header == settings.api_key:
        return api_key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )


@app.get("/")
async def root():
    return {"message": "It's working"}


@app.post("/question")
def pages(item: Item, api_key: APIKeyHeader = Depends(get_api_key)):
    question = item.question
    details = item.details
    if not question and not details:
        return {"Please provide the question and details"}
    response = get_answer(question, details)
    return {
        "question": question,
        "details": details,
        "response": response
    }


if __name__ == '__main__':
    uvicorn.run("api:app", host="0.0.0.0", port=8080, reload=True)
