from pymongo import MongoClient
from .helper import get_settings
import os

mongo_url = get_settings("mongo_url")
env = get_settings("env")
admin_db = "cloudeyes-{}".format(env)

db_connection = MongoClient(mongo_url)

def get_admin_db():
    return db_connection[admin_db]

def get_customer_db(db_name):
    return db_connection[db_name]