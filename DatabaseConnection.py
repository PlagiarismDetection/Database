from pymongo import MongoClient
from abc import ABC


class DatabaseConnection(ABC):
    @staticmethod
    def connect(CONNECTION_STRING, collection_name):
        # CONNECTION_STRING = "mongodb+srv://phuockaus:phuockaus0412@pds.qfuxg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(CONNECTION_STRING)
        return client[collection_name]
