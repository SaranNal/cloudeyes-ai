import json
import datetime
from dateutil.tz import tzutc
from collections import defaultdict
from app.db_utility import get_customer_db

with open('daily-utilization.json') as metric_file:
    metric_data = json.load(metric_file)


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
