from .DatabaseManager import DataBaseManager
from .yoloController import model

class Service:
    def __init__(self, videoDirection):
        self.read = model(videoDirection).readFrame # get the readFrame method from the model
        self.findPlaneMethod = DataBaseManager().getPlaneByClassId # Get the searching method from the database
        self.successful = True # Intended to represent whether the frame was read succesfully or not
    

    # Input: nothing
    # Returns: The Jsons of the detected objects in a list, a dictionary of the times a class appears in the frame
    def readFrame(self):
        planesNumbers = self.read()

        if planesNumbers is None:
            self.successful = False
            return [], {}

        # Get the number of planes in each class
        quantity = {}
        for plane in planesNumbers:
            if plane in quantity:
                quantity[int(plane)] += 1
            else:
                quantity[int(plane)] = 1

        return [self.findPlaneMethod(int(classNumber)) for classNumber in quantity.keys()], quantity