import json
import datetime
from dateutil.tz import tzutc
from collections import defaultdict
from app.db_utility import get_customer_db
import app.helper as helper
import sys

billing_datas = helper.retrieve_file_n_decode(sys)

for customer_id, billing_data in billing_datas.items():
    final_billing = []
    for billing in billing_data:
        billing['billing'] = {k: round(float(v), 5)
                              for k, v in billing['billing'].items()}
        final_billing.append(billing)

    customer_db = get_customer_db(customer_id)
    print(
        '----------------------------{}----------------------------'.format(customer_id))
    print('Billing data: {}'.format(
        json.dumps(final_billing)))
    daily_billing = customer_db['daily_billing']
    result = daily_billing.insert_many(final_billing)
    print('Mongo insertion id: {}'.format(result.inserted_ids))
    print('--------------------------------------------------------')
