from pymongo import MongoClient

# A Json in python is a dictionary

class DataBaseManager:
    def __init__(self):
        self.planes = MongoClient("localhost", 27017).horusTest.planes # Directly get the planes collection in the DB

    def getPlaneByClassName(self, className):
        return self.planes.find_one({"className" : className})