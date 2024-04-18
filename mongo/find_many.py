import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

from bson.objectid import ObjectId

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)
db = client.bank
account_collection = db.accounts

document_to_find = {"balance":{"$gt":4700}}

cursor = account_collection.find(document_to_find)
for rec in cursor:
    pprint.pprint(rec)

client.close()
