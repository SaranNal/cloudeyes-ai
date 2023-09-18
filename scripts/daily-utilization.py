import pandas as pd
import json
import datetime
from dateutil.tz import tzutc
from collections import defaultdict
from app.db_utility import get_customer_db

with open('service_metrics_updated.json') as metric_file:
    metric_data = json.load(metric_file)

daily_utilization_data = []
metric_data = metric_data['data']
def dict_hepler(): return defaultdict(dict_hepler)


final_metric_data = dict_hepler()
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

test = get_customer_db('test')
print(test)
daily_utilization_data.append(final_metric_data)
print(daily_utilization_data)
daily_utilization = test['daily_utilization']
result = daily_utilization.insert_many(daily_utilization_data)
print(result.inserted_ids)