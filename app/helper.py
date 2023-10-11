import openai
from functools import lru_cache
import pandas as pd
from dotenv import load_dotenv
import os
from collections import defaultdict
from dateutil.parser import parse
import json
import boto3
import hashlib
import time

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


def retrieve_file_n_decode(sys):
    # Fetching the File name
    if len(sys.argv) > 1:
        file_key = sys.argv[1]
        print(f"Processing file: {file_key}")
    else:
        print("No S3 file name provided")
        sys.exit(1)

    # Initialize the S3 client
    s3 = boto3.client('s3')
    bucket_name = get_settings()

    try:
        # Fetch the file and read its contents
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        metric_data = json.loads(obj['Body'].read().decode('utf-8'))
        return metric_data
    except json.JSONDecodeError as e:
        print("JSON decoding fail")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

def generate_chatid(account_id):
    """Generate chat id using account_id and current timestamp"""
    timestamp = str(int(time.time()))
    data = account_id + timestamp
    return hashlib.md5(data.encode()).hexdigest()