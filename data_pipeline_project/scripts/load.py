from pymongo import MongoClient

def load_to_mongo(data):
    client = MongoClient("mongodb://mongo:27017/")
    db = client["exchange_rates"]
    collection = db["rates"]

    # optional: drop existing data before inserting new
    collection.drop()

    if isinstance(data, list):
        collection.insert_many(data)
    elif isinstance(data, dict):
        collection.insert_one(data)
    else:
        raise ValueError("Unsupported data format")
