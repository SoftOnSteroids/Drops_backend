### MongoDB client ###
from pymongo import MongoClient
from os import getenv

DB_DOCKER = "DB_DEV_DOCKER_URI"
DB_DETACLOUD = "DB_DEV_DETACLOUD_URI"
uri = getenv(DB_DOCKER)
db_client = MongoClient(uri).drops

# Send a ping to confirm a successful connection
# def ping_db():
#     try:
#         print("Pinging db deployment...")
#         print(f"Response: {MongoClient(uri).admin.command('ping')}")
#         # print(f"Response: {MongoClient(uri).admin.command('ping')}")
#     except Exception as e:
#         print(e)

# ping_db()
