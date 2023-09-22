import json
import datetime
from dateutil.tz import tzutc
from collections import defaultdict
from app.db_utility import get_customer_db

with open('recommendation.json') as recommendation_file:
    recommendations_unprocessed = json.load(recommendation_file)


def dict_helper(): return defaultdict(dict_helper)

attributes = ["name", "description", "metadata"]

for customer_id, accounts_data in recommendations_unprocessed.items():
    preprocessed_recommendations = []
    processed_recommendations = dict_helper()
    for account_data in accounts_data:
        for category, data_list in account_data['recommendations'].items():
            processed_recommendations[customer_id][category] = []            
            for data in data_list:
                data_dict = {}                
                for key, val in data.items():
                    if key in attributes:
                        data_dict[key] = val
                processed_recommendations[category].append(data_dict)
    preprocessed_recommendations.append(processed_recommendations)
    
    customer_db = get_customer_db(customer_id)
    print(
        '----------------------------{}----------------------------'.format(customer_id))
    print('Security and Recommendation data: {}'.format(
        json.dumps(preprocessed_recommendations)))
    security_recommendations = customer_db['security_recommendations']
    result = security_recommendations.insert_many(preprocessed_recommendations)
    print('Mongo insertion id: {}'.format(result.inserted_ids))
    print('--------------------------------------------------------')