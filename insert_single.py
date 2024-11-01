import datetime
import os

from dotenv import load_dotenv

from pymongo import MongoClient

#load config from .env file
load_dotenv()
MONGODB_URI = "mongodb+srv://nafiou531:PyMongo123@pymongo.etphl.mongodb.net/?retryWrites=true&w=majority&appName=Pymongo"

#connect to mongodb cluster with MongoClient
client = MongoClient(MONGODB_URI)

#Get reference to PyMongo database
db = client.Pymongo
# Get reference to 'accounts' collection
accounts_collection = db.accounts

new_accounts =[
    {
    "account_number": 123456789,
    "account_type": "savings",
    "balance": 5000,
    "created_at": datetime.datetime.now(datetime.timezone.utc),
    "updated_at": datetime.datetime.now(datetime.timezone.utc),
    },
    {
    "account_number": 987654321,
    "account_type": "current",
    "balance": 10000,
    "created_at": datetime.datetime.now(datetime.timezone.utc),
    "updated_at": datetime.datetime.now(datetime.timezone.utc),
    
    }
    
]

result = accounts_collection.insert_many(new_accounts)
document_id = result.inserted_ids

print(f"Inserted document with ID: {document_id}")
client.close()