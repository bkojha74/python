import pprint
import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

client = MongoClient(MONGODB_URI)

#DB link
db = client.bank

#Collection
account_collection = db.accounts

#filter
select_accounts = {"account_type":"savings"}

#set field
set_field = {"$set":{"minimum_balance":100}}

result = account_collection.update_many(select_accounts, set_field)

print("Documents matched: "+str(result.matched_count))
print("Documents updated: "+str(result.modified_count))

pprint.pprint(account_collection.find_one(select_accounts))

client.close()