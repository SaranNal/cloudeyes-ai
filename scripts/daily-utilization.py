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
dict_hepler = lambda: defaultdict(dict_hepler)
final_metric_data = dict_hepler()
for service, metric_dict in metric_data.items():
    for instance_id, metrics in metric_dict.items():
        services = {}
        if instance_id == 'MetricDataResults':
            metrics[0]['Timestamps'] = [eval(timestamp).strftime("%m/%d/%Y") for timestamp in metrics[0]['Timestamps']]            
            final_metric_data[service] = {metrics[0]['Label'] : dict(zip(metrics[0]['Timestamps'], metrics[0]['Values']))}
        else:
            for metric in metrics['MetricDataResults']:
                metric['Timestamps'] = [eval(timestamp).strftime("%m/%d/%Y") for timestamp in metric['Timestamps']]
                final_metric_data[service][instance_id][metric['Label']] = dict(zip(metric['Timestamps'], metric['Values']))

test = get_customer_db('test')
print(test)
daily_utilization_data.append(final_metric_data)
print(daily_utilization_data)
daily_utilization = test['daily_utilization']
result = daily_utilization.insert_many(daily_utilization_data)
print(result.inserted_ids)