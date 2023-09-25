import openai
from functools import lru_cache
from pydantic_settings import BaseSettings
import pandas as pd


class Settings(BaseSettings):
    openai_key: str
    api_key: str
    env: str
    mongo_url: str

    class Config:
        env_file = "env/.env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
openai.api_key = settings.openai_key


def get_answer(question, details):
    print("Get answer for the question based on details provided...")
    res_text = resample_timeseries(details['billing'])
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": """You are a Cloud architect and Finops expert. You will respond to questions and provide recommendations based on the cloud account data provided. For cost-saving questions analyse the account data like usage, instance type and pricing. Answers should be short and specific based on the data.\n
            %s
            """ % (res_text)
            },
            {
            "role": "user",
            "content": question
            },
        ],
        temperature=1,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    res_text = response.choices[0].message.content
    print("Generated response: %s" % res_text)
    return res_text


def resample_timeseries(data):
    frame = pd.DataFrame(data)
    frame.index = pd.to_datetime(frame.index)
    # get the number of days in the timeseries
    diff = frame.index.max() - frame.index.min()
    if 0 < diff.days <= 31:
        # resample to week
        resampled_data = frame.resample('W').mean()
    elif 31 < diff.days <= 365:
        # resample to quarter start
        resampled_data = frame.resample('QS').mean()
    else:
        # resample to year start
        resampled_data = frame.resample('BAS').mean()
    return resampled_data
