from pymongo import MongoClient, errors
from .helper import get_settings
from datetime import datetime, timedelta

mongo_url = get_settings("mongo_url")
env = get_settings("env")
admin_db = "cloudeyes-{}".format(env)


def get_database(db_name):
    try:
        client = MongoClient(mongo_url)
        db_name = admin_db if db_name == 'admin' else db_name
        db = client[db_name]
        return db
    except errors.ConnectionFailure as e:
        print("MongoDB Connection Error:", e)
    except errors.PyMongoError as e:
        print("PyMongo Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


def insert_data_customer_db(customer_id, collection_name, data, delete_condition=False):
    try:
        customer_db = get_database(customer_id)
        collection = customer_db[collection_name]

        # Delete the records based on provided condition
        if delete_condition:
            collection.delete_many(delete_condition)

        # Insert the records into the collection
        record_ids = collection.insert_many(data)
        print("Inserted record:{} into collection:{} with id:{}".format(
            data, collection_name, record_ids))
        print("---------------------------------------------------")
    except errors.ConnectionFailure as e:
        print("MongoDB Connection Error:", e)
    except errors.DuplicateKeyError as e:
        print("Duplicate Key Error:", e)
    except errors.PyMongoError as e:
        print("PyMongo Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


def get_daily_data(collection, customer_db):
    """Get daily billing/utilization data for past 365 days to aggregate"""
    daily_collection = customer_db[collection]

    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    pipeline = [
        {"$match": {"date": {"$gte": start_date, "$lte": end_date}}},
        {"$sort": {"date": 1}},
        {'$project': {'_id': 0, 'date': 0, }},
        {
            "$group": {
                "_id": {"account_id": "$account_id", "tag": "$tag"},
                "data": {"$push": "$$ROOT"}
            }
        },
        {
            "$project": {
                "_id": 0,
                "account_id": "$_id.account_id",
                "tag": "$_id.tag",
                "data": 1,
            }
        }
    ]

    return daily_collection.aggregate(pipeline)
