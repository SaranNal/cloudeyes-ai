import sys
import json
import boto3
import datetime
from dateutil.tz import tzutc
# from .helper import get_settings
from collections import defaultdict
# from app.db_utility import get_customer_db
from botocore.exceptions import BotoCoreError

# get env variables
# settings = get_settings()
# print(settings)
# sys.exit(1)

# Fetching the File name
if len(sys.argv) > 1:
    file_key = sys.argv[1]
    print(f"Processing file: {file_key}")
else:
    print("No S3 file name provided")
    sys.exit(1)

# Initialize the S3 client
s3 = boto3.client('s3')
bucket_name = 'cloudeyes'

try:
    # Fetch the file and read its contents
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    metric_data = json.loads(obj['Body'].read().decode('utf-8'))
    print(file_content)
except json.JSONDecodeError as e:
    print("JSON decoding fail")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)


def dict_hepler(): return defaultdict(dict_hepler)


for customer_id, metric_datas in metric_data.items():
    for account_id, metric_data in metric_datas.items():
        daily_utilization_data = []
        final_metric_data = dict_hepler()
        final_metric_data['account_id'] = account_id
        for service, metric_dict in metric_data.items():
            for instance_id, metrics in metric_dict.items():
                is_metric_result = instance_id == 'MetricDataResults'
                service_metrics = metrics if is_metric_result else metrics[
                    'MetricDataResults']
                for metric in service_metrics:
                    metric['Timestamps'] = [eval(timestamp).strftime(
                        "%m/%d/%Y") for timestamp in metric['Timestamps']]
                    if is_metric_result:
                        final_metric_data[service][metric['Label']] = dict(
                            zip(metric['Timestamps'], metric['Values']))
                    else:
                        final_metric_data[service][instance_id][metric['Label']] = dict(
                            zip(metric['Timestamps'], metric['Values']))

        customer_db = get_customer_db(customer_id)
        daily_utilization_data.append(final_metric_data)
        print(
            '----------------------------{}----------------------------'.format(customer_id))
        print('Daily utilization data: {}'.format(
            json.dumps(daily_utilization_data)))
        daily_utilization = customer_db['daily_utilization']
        result = daily_utilization.insert_many(daily_utilization_data)
        print('Mongo insertion id: {}'.format(result.inserted_ids))
        print('--------------------------------------------------------')
