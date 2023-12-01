import json
import datetime
from dateutil.tz import tzutc
from collections import defaultdict
from app.db_utility import get_database, insert_data_customer_db
import app.helper as helper
import sys

recommendations_unprocessed = helper.retrieve_file_n_decode(sys)


def dict_helper(): return defaultdict(dict_helper)


attributes = ["name", "description", "metadata"]

for customer_records in recommendations_unprocessed:
    customer_id = customer_records['user_id']
    customer_db = get_database(customer_id)
    for accounts_data in customer_records['data']:
        preprocessed_recommendations = []
        processed_recommendations = dict_helper()
        account_id = accounts_data['account_id']
        processed_recommendations['account_id'] = account_id
        for category, data_list in accounts_data['recommendations'].items():
            processed_recommendations['recommendations'][category] = []
            for data in data_list:
                data_dict = {}
                for key, val in data.items():
                    if key in attributes:
                        data_dict[key] = val
                processed_recommendations['recommendations'][category].append(
                    data_dict)
        preprocessed_recommendations.append(processed_recommendations)

        insert_data_customer_db(customer_id, 'security_recommendations', preprocessed_recommendations, {
            'account_id': account_id})
        metadata = helper.move_processed_fie(sys)
