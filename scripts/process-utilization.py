import sys
import json
import boto3
from datetime import datetime
from dateutil.tz import tzutc
from app.helper import dict_helper
from collections import defaultdict
from app.db_utility import get_database
from botocore.exceptions import BotoCoreError
import app.helper as helper

# Retrieve and decode metric data
metric_data = helper.retrieve_file_n_decode(sys)

# Create metadata dictionaries for different services
metadata = dict_helper()
metadata['EC2'] = ['instance_type']
metadata['RDS'] = ['db_instance_type', 'db_engine']
metadata_id = {
    'EC2': 'instance_id',
    'RDS': 'db_instance_identifier'
}

# Loop through customer IDs and metric data
for customer_id, metric_datas in metric_data.items():
    daily_utilization_data = []

    # Loop through account IDs and metric data for each customer
    for account_id, metric_data in metric_datas.items():
        tmp_metric_data = final_metric_data = dict_helper()
        # Loop through services and metrics
        for services in metric_data:
            for service, metric_list in services.items():
                for metric_dict in metric_list:
                    for instance_id, metrics in metric_dict.items():
                        is_metric_result = instance_id == 'MetricDataResults'
                        if instance_id not in ['metadata', 'Messages', 'ResponseMetadata']:
                            service_metrics = metrics if is_metric_result else metrics[
                                'MetricDataResults']
                            # Loop through individual metrics
                            for metric in service_metrics:
                                for index, timestamp in enumerate(metric['Timestamps']):
                                    date = datetime.fromisoformat(
                                        timestamp.strip("'"))
                                    formatted_metric = {date.strftime(
                                        "%m/%d/%Y"): metric['Values'][index]}
                                    if is_metric_result:
                                        tmp_metric_data[date][service][metric['Label']
                                                                       ] = formatted_metric
                                    else:
                                        tmp_metric_data[date][service][instance_id][metric['Label']
                                                                                    ] = formatted_metric
                        elif instance_id == 'metadata':
                            # Add metadata for EC2 and RDS services
                            instance_id = metrics[metadata_id[service]
                                                  ] if metadata_id[service] in metrics else None
                            if instance_id:
                                tmp_metric_data[date][service][instance_id]['metadata'] = {
                                    key: metrics[key] for key in metadata[service] if key in metrics}

        # Convert data to the format that can be inserted into the database
        for metric_date, formatted_metric in tmp_metric_data.items():
            final_metric_data = formatted_metric
            final_metric_data['account_id'] = account_id
            final_metric_data['date'] = str(metric_date)
            daily_utilization_data.append(final_metric_data)

    # Insert data into the respective customer database
    print('----------------------------{}----------------------------'.format(customer_id))
    print('Daily utilization data: {}'.format(
        json.dumps(daily_utilization_data)))
    customer_db = get_database(customer_id)
    daily_utilization = customer_db['daily_utilization']
    result = daily_utilization.insert_many(daily_utilization_data)
    print('Mongo insertion id: {}'.format(result.inserted_ids))
    print('--------------------------------------------------------')
