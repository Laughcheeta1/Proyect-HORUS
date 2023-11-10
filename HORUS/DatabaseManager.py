from pymongo import MongoClient

class DataBaseManager:
    def __init__(self):
        self.planes = MongoClient("localhost", 27017).horus.Planes # Directly get the planes collection in the DB

    # Input: the class number of the desired plane
    # Returns: the Json stored in the database of that plane
    def getPlaneByClassId(self, classNumber):
        return self.planes.find_one({"classNumber" : classNumber})