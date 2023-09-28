import pandas as pd
from app.helper import dict_helper, is_date
from app.db_utility import get_admin_db, get_customer_db

# Function to resample a DataFrame to different time frequencies


def resample_timeseries(data):
    frame = pd.DataFrame(data)
    frame.index = pd.to_datetime(frame.index)
    # Calculate the time range of the time series
    time_range = frame.index.max() - frame.index.min()

    # Resample based on the time range
    if 0 < time_range.days <= 31:
        # Resample to weekly frequency
        resampled_data = frame.resample('W').mean()
    elif 31 < time_range.days <= 365:
        # Resample to quarterly frequency (start of each quarter)
        resampled_data = frame.resample('QS').mean()
    else:
        # Resample to yearly frequency (start of each year)
        resampled_data = frame.resample('BAS').mean()

    # Convert the index to periods
    resampled_data.index = resampled_data.index.to_period()
    return resampled_data


# Get the admin database
admin_db = get_admin_db()
customers = admin_db['customers'].find()

for customer in customers:
    customer_id = customer['customer_id']

    # Initialize an empty results dictionary
    results = dict_helper()
    customer_db = get_customer_db(customer_id)

    # Fetch daily utilization data
    daily_utilization = customer_db['daily_utilization']
    
    utilization_data = daily_utilization.find(
        {"account_id": "account-id-1"}, {'_id': False, 'account_id': False, 'date': False})

    # Iterate through the list of dictionaries
    for services in utilization_data:
        # Iterate through the outer keys (EFS, S3, app_runner, etc.)
        for service, inner_dict in services.items():
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
                            results[flattened_key][instance_key] = instance_value

    # Resample the results DataFrame
    resampled = resample_timeseries(results)

    # Convert the index to strings
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

    aggregated_utilization.append(reconstructed_dict)

    # Clear the existing data and insert the aggregated records
    aggregate_utilization_collection = customer_db['aggregate_utilization']
    aggregate_utilization_collection.delete_many({})
    aggregated_id = aggregate_utilization_collection.insert_many(
        aggregated_utilization)

    print("Inserted aggregated record:{} with id:{}".format(
        aggregated_utilization, aggregated_id))
