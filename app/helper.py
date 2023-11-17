import uuid
import openai
from functools import lru_cache
from dotenv import load_dotenv
import os
from collections import defaultdict
from dateutil.parser import parse
import json
import boto3
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
    bucket_name = get_settings("bucket_name")

    try:
        # Fetch the file and read its contents
        print(bucket_name)
        obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        metric_data = json.loads(obj['Body'].read().decode('utf-8'))
        return metric_data
    except json.JSONDecodeError as e:
        print("JSON decoding fail")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


def generate_chatid(account_id, question):
    """Generate chat id using account_id and current timestamp"""
    timestamp = str(int(time.time()))
    data = account_id + question + timestamp
    return str(uuid.uuid5(uuid.NAMESPACE_X500, data))


def summarize_string(input_string, max_length=50):
    """Summarize a string based on provided max_length"""
    if len(input_string) <= max_length:
        return input_string
    else:
        return input_string[:max_length - 3] + "..."


def move_processed_fie(sys):
    # Fetching the File name
    if len(sys.argv) > 1:
        source_key = sys.argv[1]
        print(f"Processing file: {source_key}")
    else:
        print("No S3 file name provided")
        sys.exit(1)

    # Initialize the S3 client
    s3 = boto3.client('s3')
    bucket_name = get_settings("bucket_name")

    try:
        # Fetch the file and read its contents
        destination_key = source_key.replace("/raw/", "/processed/")  # Replace only the first occurrence
        
        # Copy the object from the source to the destination
        s3.copy_object(
            CopySource={'Bucket': bucket_name, 'Key': source_key},
            Bucket=bucket_name,
            Key=destination_key
        )
        s3.delete_object(Bucket=bucket_name, Key=source_key)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
