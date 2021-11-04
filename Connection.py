from pymongo import MongoClient
from abc import ABC


class Connection(ABC):
    def __init__(self, CONNECTION_STRING, dbname) -> None:
        super().__init__()
        self.dbname = self.__connect(CONNECTION_STRING, dbname)

    @staticmethod
    def __connect(CONNECTION_STRING, dbname):
        # CONNECTION_STRING = "mongodb+srv://phuockaus:phuockaus0412@pds.qfuxg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        client = MongoClient(CONNECTION_STRING)
        return client[dbname]

    def getDatabase(self):
        return self.dbname
