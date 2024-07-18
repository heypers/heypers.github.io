from core import Config
from pymongo import MongoClient
import certifi


class Database:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI, connect=False, tlsCAFile=certifi.where())
        self.DB = self.client.kayadb

    @staticmethod
    def check_entry(collection, query, param):
        entry = collection.find_one(query)
        if entry is None:
            collection.insert_one({**query, **param})
        else:
            collection.update_one(query, {"$set": param}, upsert=True)