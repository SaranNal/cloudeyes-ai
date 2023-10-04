import openai
from functools import lru_cache
import pandas as pd
from dotenv import load_dotenv
import os
from collections import defaultdict
from dateutil.parser import parse

# Specify the path to your .env file
dotenv_path = '.env'

# Load variables from the custom .env file
load_dotenv(dotenv_path)


@lru_cache()
def get_settings(setting):
    return os.getenv(setting)


openai.api_key = get_settings("api_key")


def get_answer(question, details):
    print("Get answer for the question based on details provided...")
    res_text = ""
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


def dict_helper(): return defaultdict(dict_helper)


def is_date(string):
    try:
        parse(string, fuzzy=False)
        return True

    except ValueError:
        return False
