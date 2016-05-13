# Definition of base controller
from app.model.modelBase import *


class controllerBase:
    def __init__(self, controllerData, controllerType):
        # print "controller Base Enter:", controllerType
        self.controllermodellist = []
        for(k,v) in controllerData.items():
            model = modelBase(v,controllerType)
            self.controllermodellist.append(model)
        # print("controller Base End: "), controllerType

    def printController(self):
        print " "
        print "----------Print Controller Start"
        for model in self.controllermodellist:
            model.printModel()
        print "----------Print Controller End"

    def executeController(self):
        print "Implement the executation of Controller"

    def clearController(self):
        print "Implement the clean of running Controller"

    def getControllerStatus(self):
        print "Implement get Controller status"
