# Controller of Bridge Interfaces

from app.model.brInterfaces import *


class ControllerBrInterfaces:
    def __init__(self):
        print("Controller Bridge Interfaces Init")

    def initBridgeInterfaces(self, interfaces):
        self.brInterfacesList = []
        print type(interfaces)

        for(k,v) in interfaces.items():
            print type(k),"=",k, type(v)
            brintf = BrInterfaces()
            brintf.initBridgeInterface(v)
            self.brInterfacesList.append(brintf)

    def sayHello(self):
        print("Test Hello")

    def printBridgeInterfaces(self):
        for brintf in self.brInterfacesList:
            brintf.printBridgeInterface()