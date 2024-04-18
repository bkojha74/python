import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)
db = client.bank
account_collection = db.accounts

new_account = {
    "account_holder": "Bipin Ojha",
    "account_id": "MDB829001339",
    "account_type": "checking",
    "balance": 50352434,
    "last_updated": datetime.datetime.utcnow(),
}

result = account_collection.insert_one(new_account)
document_id = result.inserted_id

print(f"_id of inserted document: {document_id}")

client.close()
