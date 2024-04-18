import os
import pprint

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)
db = client.bank
account_collection = db.accounts

document_to_delete = {"balance":{"$gt":4700}}

#search for sample document before delete
print("searching for sample document before delete:")
pprint.pprint(account_collection.find_one(document_to_delete))

result = account_collection.delete_many(document_to_delete)

#search for sample document after delete
print("searching for sample document after delete:")
pprint.pprint(account_collection.find_one(document_to_delete))

print("Documents deleted: " + str(result.deleted_count))

client.close()
