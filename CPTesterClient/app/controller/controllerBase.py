# Definition of base controller
from app.model.modelBase import *
from app.model.modelTypes import *

class controllerBase:
    def __init__(self, controllerData, controllerType):
        print "controller Base Enter:", controllerType
        # print type(controllerData)
        # print type(controllerType)
        self.controllermodellist = []
        for(k,v) in controllerData.items():
            # print type(k),"=",k, type(v)
            model = modelBase(v,modelTypes[controllerType])
            # brintf.initModel(v)
            self.controllermodellist.append(model)
        print("controller Base End: "), controllerType

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
