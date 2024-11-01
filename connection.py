from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://nafiou531:PyMongo123@pymongo.etphl.mongodb.net/?retryWrites=true&w=majority&appName=Pymongo"

client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
    print(db_name)