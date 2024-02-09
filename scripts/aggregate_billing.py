import json
import pandas as pd
from app.helper import dict_helper, is_date
from app.db_utility import get_daily_data, get_database, insert_data_customer_db
from datetime import datetime, timedelta
from app.openai_helper import count_number_of_token


def aggregate_billing():
    # Get the admin database
    admin_db = get_database('admin')
    customers = admin_db['customers'].find()

    for customer in customers:
        customer_id = customer['customer_id']
        print("Aggregating billing data for customer: {}".format(customer_id))
        customer_db = get_database(customer_id)
        billing_data = get_daily_data('daily_billing', customer_db)

        # Iterate through the list of dictionaries
        for accounts in billing_data:
            aggregated_billing = []
            restructured_data = {}
            account_id = accounts['account_id'] if 'account' in accounts else ""
            tag = accounts['tag'] if 'tag' in accounts else ""
            for entry in accounts["data"]:
                restructured_data[entry['date']] = entry['billing']

            # Create a DataFrame from the data
            billing_df = pd.DataFrame(restructured_data)
            billing_df = billing_df.transpose()

            # # Calculate the mean for the last 12 months and 30 days
            last_12_months_mean = billing_df.sum()
            last_30_days_mean = billing_df.tail(30).sum()

            mean_values = {
                'last_12_months': last_12_months_mean.round(2),
                'last_30_days': last_30_days_mean.round(2)
            }
            aggregated_billing_data = pd.DataFrame(mean_values).transpose()
            aggregated_billing_data = aggregated_billing_data.to_dict()
            # remove tax and support from billing data
            if 'Tax' in aggregated_billing_data:
                del aggregated_billing_data['Tax']
            if 'AWS Support (Business)' in aggregated_billing_data:
                del aggregated_billing_data['AWS Support (Business)']
            aggregated_billing_data['token_size'] = count_number_of_token(
                json.dumps(aggregated_billing_data, separators=(',', ':')), 'cl100k_base')
            aggregated_billing_data['account_id'] = account_id
            aggregated_billing_data['tag'] = tag

            aggregated_billing.append(aggregated_billing_data)
            insert_data_customer_db(customer_id, 'aggregate_billing', aggregated_billing, {
                                    'account_id': account_id, 'tag': tag})

    print("Aggregated billing data for all the customers")
