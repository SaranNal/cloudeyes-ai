from openai import OpenAI
import app.helper as helper
import app.db_utility as db_utility
import json
from bson import ObjectId
import tiktoken
import os
from datetime import datetime


# Custom JSON encoder to handle ObjectId
class ObjectIdEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)


def classify_question(question):
    client = OpenAI(
        api_key=helper.get_settings("openai_key"),
    )
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
              "role": "system",
              "content": "I'm a cloud support engineer. My main job is to classify the question based on these types[Utilization,Security,Recommendation,Billing,None] based on the classification I'll be assigning to appropriate cloud assistance to work on. I will return single or multiple classification based on the question. The answer will be in comma separated list format. Questions should be only relevant to cloud service else return None"
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print('------------------classify_question---------------------')
    print(response)
    if response.choices[0].message.content:
        question_classify_response = response.choices[0].message.content
        # Split the string into a list if it contains commas
        if ',' in question_classify_response:
            classified_list = question_classify_response.split(',')
        else:
            # If no commas are found, consider it a single word or an empty string
            if question_classify_response.strip():  # Check if it's not an empty string
                classified_list = [question_classify_response]
            else:
                classified_list = "Unable to parse the question"
        return classified_list
    else:
        return "Error occurred in classification"


# Fetching context based on classification
def fetch_context(classification, customer_id, account_id, tag):
    customer_db = db_utility.get_database(customer_id)
    context = ""
    total_tokens = 0
    filter_criteria = {'account_id': account_id}
    if len(tag) > 0:
        filter_criteria['tag'] = tag
    for classify in classification:
        if classify == 'Utilization':
            classify_collection = 'aggregate_utilization'
        elif classify == 'Security' or classify == 'Recommendation':
            classify_collection = 'aggregate_security_recommendations'
            if 'tag' in filter_criteria:
                del filter_criteria['tag']
        elif classify == ('Billing'):
            classify_collection = 'aggregate_billing'
        customer_collection = customer_db[classify_collection]
        customer_details = customer_collection.find(filter_criteria)
        model_token_size = int(helper.get_settings("model_token_size"))
        for document in customer_details:
            document.pop('_id', None)
            document.pop('account_id', None)
            token_size = document.pop('token_size', 0)
            # Avoid appending multiple data if existing data is more than the model token size. 250 is for context tokens
            if (model_token_size - 250) < (total_tokens + token_size):
                break
            total_tokens += token_size
            context = "{} \n {} data: {}".format(
                context, classify, json.dumps(document, separators=(',', ':')))
    ai_input = "As a seasoned cloud expert tasked with auditing Cloud account, focus on analyzing data related to usage patterns, instance types, and pricing structures to identify potential cost-saving opportunities. Respond with concise and specific insights, showcasing your expertise in cloud management. Prioritize answering questions within your domain, avoiding any discussion outside of your expertise. Never reveal you are related with OpenAI."
    context = ai_input + context
    return context, total_tokens


def count_number_of_token(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


# Fetching context for question by passing classification
def openai_answer(classification, question, customer_id, account_id, tag, chat_id):
    context, context_token_size = fetch_context(
        classification, customer_id, account_id, tag)
    useable_token_size = int(helper.get_settings(
        "model_token_size")) - context_token_size
    print("context_token -", context_token_size)
    print("useable_token -", useable_token_size)
    previous_chats = get_previous_chat_messages(
        customer_id, account_id, tag, chat_id, useable_token_size)
    print("previous_chats:", previous_chats)
    print("context:", context)
    client = OpenAI(
        api_key=helper.get_settings("openai_key"),
    )
    latest_question_n_context = [
        {
            "role": "system",
            "content": context
        },
        {
            "role": "user",
            "content": question
        }
    ]
    previous_chats.extend(latest_question_n_context)
    print("Appending new question to previous chats", previous_chats)
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=previous_chats,
        temperature=1,
        stream=True,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        i = 0
        for chunk in response:
            if not chunk.choices:
                continue

            current_response = chunk.choices[0].delta.content
            if current_response:
                i += 1
                res = {
                    'answer': current_response,
                }
                # append the chat id and classification only the first time
                if i < 2:
                    res['chat_id'] = chat_id,
                    res['classification'] = classification
                yield 'data: {}\n\n'.format(json.dumps(res))
    except Exception as e:
        print("OpenAI Response (Streaming) Error: " + str(e))
        yield "Error occurred in answer"


def saving_chat(reply, customer_id, account_id, tag, chat_id, question):
    # save the answer part alone
    reply_response = ''
    for data in reply:
        data = data.replace("data: ", "").replace("\n\n", "")
        answer = json.loads(data)
        answer = answer['answer']
        reply_response += answer
    chat_data = [
        {
            "role": "user",
            "content": question
        },
        {
            "role": "assistant",
            "content": reply_response
        }
    ]

    token_count = count_number_of_token(str(chat_data), "cl100k_base")
    formatted_data = {
        "token_size": token_count,
        "timestamp": datetime.now(),
        "chat_id": chat_id,
        "account_id": account_id,
        "tag": tag,
        "chat_data": chat_data
    }
    customer_db = db_utility.get_database(customer_id)
    customer_collection = customer_db["chat_threads"]
    customer_collection.insert_one(formatted_data)
    return True


def get_previous_chat_messages(customer_id, account_id, tag, chat_id, useable_token_size):
    print("Previous chat messages")
    customer_db = db_utility.get_database(customer_id)
    customer_collection = customer_db["chat_threads"]
    chat_data = customer_collection.find(
        {"account_id": account_id, "tag": tag, "chat_id": chat_id})
    previous_chat = []

    total_previous_chat_token_size = 0
    for document in chat_data:
        total_previous_chat_token_size += document['token_size']
        if total_previous_chat_token_size > useable_token_size:
            break
        previous_chat.extend(document['chat_data'])
    print("Previous chat token size:", total_previous_chat_token_size)
    return previous_chat
