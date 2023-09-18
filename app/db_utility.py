from pymongo import MongoClient
from .helper import get_settings

# get env variables
settings = get_settings()

mongo_url = settings.mongo_url
db_connection = MongoClient(mongo_url)

def get_admin_db():
    return db_connection.admin_db

def get_customer_db(db_name):
    return db_connection[db_name]