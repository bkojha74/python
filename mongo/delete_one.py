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

document_to_delete = {"_id":ObjectId("65f9752534617ca48a45f7b9")}

result = account_collection.delete_one(document_to_delete)
pprint.pprint(result)

client.close()