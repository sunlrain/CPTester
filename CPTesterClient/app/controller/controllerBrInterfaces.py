# Controller of Bridge Interfaces

from app.controller.controllerBase import *


class ControllerBrInterfaces(controllerBase):
    def sayhello(self):
        print "Hello"

    def executeController(self):
        self.sayhello()
    # def __init__(self):
    #     print("Controller Bridge Interfaces Init")

    # def initBridgeInterfaces(self, interfaces):
    #     self.brInterfacesList = []
    #     print type(interfaces)
    #
    #     for(k,v) in interfaces.items():
    #         print type(k),"=",k, type(v)
    #         brintf = modelBrInterfaces()
    #         brintf.initModel(v)
    #         # brintf.initBridgeInterface(v)
    #         self.brInterfacesList.append(brintf)
    #
    # def printBridgeInterfaces(self):
    #     for brintf in self.brInterfacesList:
    #         brintf.printModel()
    #         # brintf.printBridgeInterface()