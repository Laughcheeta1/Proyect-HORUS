from DatabaseManager import DataBaseManager
from yoloController import model

class Service:
    def __init__(self, videoDirection):
        self.yoloModel = model(videoDirection).readFrame # get the readFrame method from the model
        self.findPlaneMethod = DataBaseManager().getPlaneByClassId # Get the searching method from the database
    

    # Input: nothing
    # Returns: The Jsons of the detected objects in a list, a dictionary of the times a class appears in the frame
    def readFrame(self):
        planesNumbers = self.yoloModel.readFrame()

        quantity = {} # Get the number of planes in each class
        for plane in planesNumbers:
            if plane in quantity:
                quantity[plane] += 1
            else:
                quantity[plane] = 1

        return [self.findPlaneMethod(classNumber) for classNumber in quantity.keys()], quantity