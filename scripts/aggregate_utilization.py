import json
import pandas as pd
from app.helper import dict_helper, is_date
from app.db_utility import get_database, insert_data_customer_db
from datetime import datetime, timedelta
from app.openai_helper import count_number_of_token


def aggregate_timeseries(data, range='year'):
    """Function to aggregate a DataFrame to different time frequencies"""
    frame = pd.DataFrame(data)
    # frame.index = pd.to_datetime(frame.index)

    # range_mapping = {
    #     'year': 365,
    #     'month': 30,
    #     'week': 7
    # }
    # filtered_frame = frame[frame.index > frame.index.max(
    # ) - pd.DateOffset(days=range_mapping[range])]

    # Calculate the mean for the last 12 months and 30 days
    last_12_month_mean = frame.mean().fillna(0)
    last_30_days_mean = frame.tail(30).mean().fillna(0)

    mean_values = {
        'last_12_months': last_12_month_mean.round(2),
        'last_30_days': last_30_days_mean.round(2)
    }
    resampled_data = pd.DataFrame(mean_values).transpose()
    return resampled_data


def aggregate_utilization():
    # Get the admin database
    admin_db = get_database('admin')
    customers = admin_db['customers'].find()

    for customer in customers:
        customer_id = customer['customer_id']
        print("Aggregating utilization data for customer: {}".format(customer_id))
        customer_db = get_database(customer_id)
        daily_utilization = customer_db['daily_utilization']

        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        pipeline = [
            {"$match": {"date": {"$gte": start_date, "$lte": end_date}}},
            {"$sort": {"date": 1}},
            {'$project': {'_id': 0, 'date': 0, }},
            {
                "$group": {
                    "_id": "$account_id",
                    "data": {"$push": "$$ROOT"}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "account_id": "$_id",
                    "data": 1,
                }
            }
        ]
        utilization_data = daily_utilization.aggregate(pipeline)

        # Iterate through the list of dictionaries
        for accounts in utilization_data:
            results = dict_helper()
            account_id = accounts['account_id']
            for services in accounts['data']:
                # Iterate through the outer keys (EFS, S3, app_runner, etc.)
                for service, inner_dict in services.items():
                    if service != 'account_id':
                        # Iterate through the inner keys (PercentIOLimit, StorageBytes, etc.)
                        for inner_key, instance_dict in inner_dict.items():
                            # Iterate through the date keys (09/01/2022, 09/02/2022, etc.)
                            for date_key, value in instance_dict.items():
                                # Create a flattened key by combining outer_key and inner_key
                                if is_date(date_key):
                                    flattened_key = f"{service}|{inner_key}"
                                    # Add the flattened key and value to the result dictionary
                                    results[flattened_key][date_key] = value
                                else:
                                    for instance_key, instance_value in value.items():
                                        flattened_key = f"{service}|{inner_key}|{date_key}"
                                        # Add the flattened key and value to the result dictionary
                                        if is_date(instance_key):
                                            results[flattened_key][instance_key] = instance_value

            resampled = aggregate_timeseries(results)
            resampled.index = resampled.index.astype(str)
            # Convert the resampled DataFrame to a dictionary
            resampled = resampled.to_dict()
            aggregated_utilization = []

            # Split keys by "|" and create a nested dictionary
            reconstructed_dict = {}
            for key, value in resampled.items():
                keys = key.split("|")
                current_dict = reconstructed_dict
                for k in keys[:-1]:
                    current_dict = current_dict.setdefault(k, {})
                current_dict[keys[-1]] = value

            reconstructed_dict['token_size'] = count_number_of_token(
                json.dumps(reconstructed_dict, separators=(',', ':')), 'cl100k_base')
            reconstructed_dict['account_id'] = account_id
            aggregated_utilization.append(reconstructed_dict)

            insert_data_customer_db(customer_id, 'aggregate_utilization', aggregated_utilization, {
                                    'account_id': account_id})

    print("Aggregated utilization data for all customers")
