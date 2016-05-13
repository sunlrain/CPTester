# Definition of base model
from modelTypes import *


class modelBase:
    def __init__(self, modelData, modelKeys):
        self.keys = modelTypes[modelKeys]
        self.data = modelData

    def printModel(self):
        print " "
        for key in self.keys:
            print key, ":", self.data[key]