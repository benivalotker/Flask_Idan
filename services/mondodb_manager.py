import config
import pymongo


def get_connection():
    client = pymongo.MongoClient(config.mongodb_uri)

    db = client[config.mongodb_db]

    return db


def get_data(collection, query):
    db = get_connection()
    collection = db[collection]

    return collection.find_one(query)
