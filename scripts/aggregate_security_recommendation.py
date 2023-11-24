import json
from app.db_utility import get_database, insert_data_customer_db
import os


def aggregated_security_recommendation():
    admin_db = get_database('admin')
    customers = admin_db['customers'].find()
    try:
        for customer in customers:
            customer_id = customer['customer_id']
            customer_db = get_database(customer_id)
            security_recommendation_data = customer_db['security_recommendations']

            for account_data in security_recommendation_data.find():
                account_id = account_data['account_id']
                recommendation = account_data['recommendations']
                new_formatted_data = {
                    "$set": {
                        "account_id": account_id,
                        "security_recommendation": "",
                        "cost_optimizing": ""
                    }
                }
                if "security" in recommendation:
                    security_recommendation = [d['name']
                                               for d in recommendation['security']]
                    new_formatted_data['$set']['security_recommendation'] = security_recommendation
                if "cost_optimizing" in recommendation:
                    cost_optimizing = [d['name']
                                       for d in recommendation['cost_optimizing']]
                    new_formatted_data['$set']['security_recommendation'] = cost_optimizing
                filter_criteria = {"account_id": account_id}
                agg_security_recommendation_data = customer_db['aggregate_security_recommendations']
                result = agg_security_recommendation_data.update_one(
                    filter_criteria, new_formatted_data, upsert=True)
                print(
                    f"Matched {result.modified_count} document(s) and updated {result.modified_count} document(s).")
    except Exception as e:
        print(f"An error occurred: {e}")
