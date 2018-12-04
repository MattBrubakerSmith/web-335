import pymongo
import pprint
import datetime

client = pymongo.MongoClient("localhost", 27017)

db = client.web335

user = {
    "first_name": "Gary",
    "last_name": "Busey",
    "email": "somethingunintelligible@grrrwl.clom",
    "employee_id": "9111111",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "9111111"}))