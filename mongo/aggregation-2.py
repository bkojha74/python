import pprint
import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)
db = client.bank

account_collection = db.accounts

conversion_rate_usd_to_gbp = 1.3

select_accounts = {"$match":{"account_type":"checking", "balance":{"$gt":1500}}}

organise_by_original_balance = {"$sort":{"balance":-1}}

return_specified_fields = {
    "$project":{
        "account_type":1,
        "balance":1,
        "gbp_balance":{"$divide":["$balance", conversion_rate_usd_to_gbp]},
        "_id":0,
    }
}

pipeline = [select_accounts, organise_by_original_balance, return_specified_fields]

results = account_collection.aggregate(pipeline)

print()
print("Account Type")

for item in results:
    pprint.pprint(item)

client.close()