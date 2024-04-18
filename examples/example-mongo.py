from dotenv import load_dotenv
from pymongo import MongoClient
import os
import pprint
from bson.objectid import ObjectId

x = load_dotenv()
y = os.getenv["MONGODB_URI"]

client = MongoClient(y)
db = client.bank
col = db.account

qry1 = {"_id":ObjectId("XXXXXXXXXXXXXXXXX")}
qry2 = {"balance": {"$gt":5000}}
qry3 = {"$inc": {"balance":100}}
qry4 = {"balance":100}

z = col.find_one(qry1)
pprint.pprint(z)

cur = col.find(qry2)
for rec in cur:
    pprint.pprint(rec)

result = col.update_one(qry1, qry3)
pprint.pprint(result.modified_count)

result = col.update_many(qry4, qry3)
pprint.pprint(result.modified_count)

client.close()
