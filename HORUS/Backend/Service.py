from DatabaseManager import DataBaseManager

class Service:
    def __init__(self):
        self.findPlaneMethod = DataBaseManager().getPlaneByClassName
    
    # Receives a list of the classNames of the found planes
    def getPlanes(self, classNames):
        return [self.findPlaneMethod(className) for className in classNames]