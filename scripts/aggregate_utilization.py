import json
import pandas as pd
from app.helper import dict_helper, is_date
from app.db_utility import get_daily_data, get_database, insert_data_customer_db
from datetime import datetime, timedelta
from app.openai_helper import count_number_of_token


def aggregate_timeseries(data):
    """Function to aggregate a DataFrame to different time frequencies"""
    frame = pd.DataFrame(data)

    # Calculate the mean for the last 12 months and 30 days
    last_12_month_mean = frame.mean().fillna(0)
    last_30_days_mean = frame.tail(30).mean().fillna(0)

    mean_values = {
        'last_12_months': last_12_month_mean.round(2),
        'last_30_days': last_30_days_mean.round(2)
    }
    resampled_data = pd.DataFrame(mean_values).transpose()
    return resampled_data


def reconstruct_dict(flattened_dict):
    """Split keys by "|" and create a nested dictionary"""
    reconstructed_dict = {}
    for key, value in flattened_dict.items():
        keys = key.split("|")
        current_dict = reconstructed_dict
        for k in keys[:-1]:
            current_dict = current_dict.setdefault(k, {})
        current_dict[keys[-1]] = value
    return reconstructed_dict


def merge_dicts(dict1, dict2):
    """Recursively merge two dictionaries with multiple levels."""
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict and isinstance(merged_dict[key], dict) and isinstance(value, dict):
            merged_dict[key] = merge_dicts(merged_dict[key], value)
        else:
            merged_dict[key] = value
    return merged_dict


def aggregate_utilization():
    # Get the admin database
    admin_db = get_database('admin')
    customers = admin_db['customers'].find()

    for customer in customers:
        customer_id = customer['customer_id']
        print("Aggregating utilization data for customer: {}".format(customer_id))
        customer_db = get_database(customer_id)
        utilization_data = get_daily_data('daily_utilization', customer_db)

        # Iterate through the list of dictionaries
        for accounts in utilization_data:
            results = dict_helper()
            metadata_dict = dict_helper()
            account_id = accounts['account_id']
            tag = accounts['tag'] if 'tag' in accounts else ''
            for services in accounts['data']:
                # Iterate through the outer keys (EFS, S3, app_runner, etc.)
                for service, inner_dict in services.items():
                    if service not in ['account_id', 'tag']:
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
                                        else:
                                            metadata_dict[flattened_key][instance_key] = instance_value

            resampled = aggregate_timeseries(results)
            resampled.index = resampled.index.astype(str)
            # Convert the resampled DataFrame to a dictionary
            resampled = resampled.to_dict()
            aggregated_utilization = []

            resampled_dict = reconstruct_dict(resampled)
            reconstructed_metadata = reconstruct_dict(metadata_dict)
            final_aggregated_data = merge_dicts(
                resampled_dict, reconstructed_metadata)

            final_aggregated_data['token_size'] = count_number_of_token(
                json.dumps(final_aggregated_data, separators=(',', ':')), 'cl100k_base')
            final_aggregated_data['account_id'] = account_id
            final_aggregated_data['tag'] = tag
            aggregated_utilization.append(final_aggregated_data)
            insert_data_customer_db(customer_id, 'aggregate_utilization', aggregated_utilization, {
                                    'account_id': account_id, 'tag': tag})

    print("Aggregated utilization data for all customers")
