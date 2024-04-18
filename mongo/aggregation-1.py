import pprint
import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)
db = client.bank

account_collection = db.accounts

select_by_balance = {"$match":{"balance":{"$lt":1000}}}

separate_by_account_calculate_avg_balance = {"$group":{"_id":"$account_type", "avg_balance":{"$avg":"$balance"}}}

pipeline = [select_by_balance, separate_by_account_calculate_avg_balance]

results = account_collection.aggregate(pipeline)

print()
print("Average Balance checking for balance less than 1000")

for item in results:
    pprint.pprint(item)

client.close()