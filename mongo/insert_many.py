import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)
db = client.bank
account_collection = db.accounts

new_account = [{
    "account_holder": "Itita Ojha",
    "account_id": "MDB829001338",
    "account_type": "savings",
    "balance": 50000.00,
    "last_updated": datetime.datetime.utcnow(),
},
{
    "account_holder": "Nandita Ojha",
    "account_id": "MDB829001337",
    "account_type": "current",
    "balance": 10.00,
    "last_updated": datetime.datetime.utcnow(),
}]

result = account_collection.insert_many(new_account)
document_ids = result.inserted_ids

print(f"{str(len(document_ids))} of documents inserted. _id of inserted document: {document_ids}")

client.close()
