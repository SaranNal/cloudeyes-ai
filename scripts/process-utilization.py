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

metric_data = helper.retrieve_file_n_decode(sys)


for customer_id, metric_datas in metric_data.items():
    daily_utilization_data = []
    for account_id, metric_data in metric_datas.items():
        tmp_metric_data = final_metric_data = dict_helper()
        for services in metric_data:
            for service, metric_list in services.items():
                for metric_dict in metric_list:
                    for instance_id, metrics in metric_dict.items():
                        is_metric_result = instance_id == 'MetricDataResults'
                        if instance_id not in ['metadata', 'Messages', 'ResponseMetadata']:
                            service_metrics = metrics if is_metric_result else metrics[
                                'MetricDataResults']
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

        for metric_date, formatted_metric in tmp_metric_data.items():
            final_metric_data = formatted_metric
            final_metric_data['account_id'] = account_id
            final_metric_data['date'] = str(metric_date)
            daily_utilization_data.append(final_metric_data)

    print(
        '----------------------------{}----------------------------'.format(customer_id))
    print('Daily utilization data: {}'.format(
        json.dumps(daily_utilization_data)))
    customer_db = get_database(customer_id)
    daily_utilization = customer_db['daily_utilization']
    result = daily_utilization.insert_many(daily_utilization_data)
    print('Mongo insertion id: {}'.format(result.inserted_ids))
    print('--------------------------------------------------------')
