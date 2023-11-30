import json
import datetime
from dateutil.tz import tzutc
from collections import defaultdict
from app.db_utility import get_database
import app.helper as helper
import sys

recommendations_unprocessed = helper.retrieve_file_n_decode(sys)


def dict_helper(): return defaultdict(dict_helper)


attributes = ["name", "description", "metadata"]

for customer_records in recommendations_unprocessed:
    preprocessed_recommendations = []
    processed_recommendations = dict_helper()
    for accounts_data in customer_records['data']:
        customer_id = customer_records['user_id']
        account_id = accounts_data['account_id']
        processed_recommendations[account_id]['account_id'] = account_id
        for category, data_list in accounts_data['recommendations'].items():
            processed_recommendations[account_id][category] = []
            for data in data_list:
                data_dict = {}
                for key, val in data.items():
                    if key in attributes:
                        data_dict[key] = val
                processed_recommendations[account_id][category].append(
                    data_dict)
    preprocessed_recommendations.append(processed_recommendations)

    customer_db = get_database(customer_id)

    print(
        '----------------------------{}----------------------------'.format(customer_id))
    print('Security and Recommendation data: {}'.format(
        json.dumps(preprocessed_recommendations)))
    security_recommendations = customer_db['security_recommendations']
    result = security_recommendations.insert_many(preprocessed_recommendations)
    print('Mongo insertion id: {}'.format(result.inserted_ids))
    print('--------------------------------------------------------')
    metadata = helper.move_processed_fie(sys)
