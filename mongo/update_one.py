import pprint
import os

from dotenv import load_dotenv
from pymongo import MongoClient

from bson.objectid import ObjectId

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)
db = client.bank
account_collection = db.accounts

document_to_update = {"_id": ObjectId("65f975b2cfe64c4019b1ebc8")}

add_to_balance={"$inc":{"balance":100}}

result = account_collection.update_one(document_to_update, add_to_balance)

print("Documents updated: "+str(result.modified_count))

pprint.pprint(account_collection.find_one(document_to_update))

client.close()