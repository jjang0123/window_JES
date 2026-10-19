from abc import ABC, abstractmethod

class Polygon(ABC):
    shapes = {3: 'triangle', 4: 'rectangle', 5: 'pentagon'}

    def __init__(self, numSide):
        self.sideNumber = numSide
        self.sideLen = 0

    def setSideLen(self, sideLen):
        self.sideLen = float(sideLen)

    def getShape(self):
        return Polygon.shapes[self.sideNumber]

    @abstractmethod
    def getArea(self):
        pass
