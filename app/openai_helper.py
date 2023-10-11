import openai
import app.helper as helper
import app.db_utility as db_utility
import json
from bson import ObjectId


# Custom JSON encoder to handle ObjectId
class ObjectIdEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)


def classify_question(question):
    openai.api_key = helper.get_settings("openai_key")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
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
    if response['choices'][0]['message']['content']:
        question_classify_response = response['choices'][0]['message']['content']
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
        return "Error occurred"


# Fetching context for question by passing classification
def openai_answer(classification, question, customer_id, account_id, chat_id):
    context = fetch_context(classification, customer_id, account_id)
    openai.api_key = helper.get_settings("openai_key")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
              "role": "system",
              "content": context
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

    return response


# Fetching context based on classification
def fetch_context(classification, customer_id, account_id):
    customer_db = db_utility.get_database(customer_id)
    context = ""

    for classify in classification:
        if classify == 'Utilization':
            classify_collection = 'aggregate_utilization'
        elif classify == ('Security' or 'Recommendation'):
            classify_collection = 'security_recommendations'
        elif classify == ('Billing'):
            classify_collection = 'aggregate_billing'
        customer_collection = customer_db[classify_collection]
        customer_details = customer_collection.find({'account_id': account_id})
        for document in customer_details:
            if '_id' in document: del document['_id']
            if 'account_id' in document: del document['account_id']
            context = "{} \n {} data: {}".format(context, classify, json.dumps(document))
    ai_input = "You are a cloud cost expert. You will be auditing aws account and analyzing data. For cost-saving questions analyse the account data like usage, instance type and pricing. Your answer should be short and specific."
    context = ai_input + context
    return context
