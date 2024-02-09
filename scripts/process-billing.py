import json
import datetime
from dateutil.tz import tzutc
from collections import defaultdict
from app.db_utility import get_database
from app.helper import dict_helper, retrieve_file_n_decode, move_processed_fie
import sys
from datetime import datetime

billing_datas = retrieve_file_n_decode(sys)

for customer_id, accounts_list in billing_datas.items():
    final_billing = []
    for account in accounts_list:
        if account['billing']:
            for billing_data in account['billing']:
                for billing_date, billing in billing_data.items():
                    final_billing_data = dict_helper()
                    final_billing_data['account_id'] = account['account_id']
                    final_billing_data['tag'] = account['tag'] if 'tag' in account else ''
                    final_billing_data['date'] = datetime.strptime(
                        billing_date, '%Y-%m-%d')
                    final_billing_data['billing'] = {k: round(float(v), 5)
                                                     for k, v in billing.items()}
                    final_billing.append(final_billing_data)

    if final_billing:
        customer_db = get_database(customer_id)
        print(
            '----------------------------{}----------------------------'.format(customer_id))
        print('Billing data: {}'.format(json.dumps(final_billing, default=str)))
        daily_billing = customer_db['daily_billing']
        result = daily_billing.insert_many(final_billing)
        print('Mongo insertion id: {}'.format(result.inserted_ids))
        print('--------------------------------------------------------')
metadata = move_processed_fie(sys)
