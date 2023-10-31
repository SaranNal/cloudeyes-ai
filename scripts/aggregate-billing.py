import json
import pandas as pd
from app.helper import dict_helper, is_date
from app.db_utility import get_database, insert_data_customer_db
from datetime import datetime, timedelta
from app.openai_helper import count_number_of_token

# Get the admin database
admin_db = get_database('admin')
customers = admin_db['customers'].find()

for customer in customers:
    customer_id = customer['customer_id']
    customer_db = get_database(customer_id)
    daily_billing = customer_db['daily_billing']

    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    pipeline = [
        {"$match": {"date": {"$gte": start_date, "$lte": end_date}}},
        {'$project': {'_id': 0, }},
        {
            "$group": {
                "_id": "$account_id",
                "data": {"$push": "$$ROOT"}
            }
        },
        {
            "$project": {
                "_id": 0,
                "account_id": "$_id",
                "data": 1,
            }
        }
    ]
    billing_data = daily_billing.aggregate(pipeline)

    # Iterate through the list of dictionaries
    for accounts in billing_data:
        aggregated_billing = []
        restructured_data = {}
        account_id = accounts['account_id']
        for entry in accounts["data"]:
            restructured_data[entry['date']] = entry['billing']

        # Create a DataFrame from the data
        billing_df = pd.DataFrame(restructured_data)
        billing_df = billing_df.transpose()

        # # Calculate the mean for the last 12 months and 30 days
        last_12_months_mean = billing_df.last("12M").mean()
        last_30_days_mean = billing_df.last("30D").mean()

        mean_values = {
            'last_12_months': last_12_months_mean.round(2),
            'last_30_days': last_30_days_mean.round(2)
        }
        aggregated_billing_data = pd.DataFrame(mean_values).transpose()
        aggregated_billing_data = aggregated_billing_data.to_dict()
        aggregated_billing_data['token_size'] = count_number_of_token(
            json.dumps(aggregated_billing_data, separators=(',', ':')), 'cl100k_base')
        aggregated_billing_data['account_id'] = account_id

        aggregated_billing.append(aggregated_billing_data)

        insert_data_customer_db(customer_id, 'aggregate_billing', aggregated_billing, {
                                'account_id': account_id})

print("Aggregated billing data for all the customers")
