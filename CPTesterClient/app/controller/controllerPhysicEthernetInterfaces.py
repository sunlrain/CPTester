# Controller for physic Ethernet interfaces
from app.controller.controllerBase import *
from app.utils.utilPhysicEthernetInterface import *


class ControllerPhysicEthernetInterfaces(controllerBase):
    def sayhello(self):
        print "Hello"

    def executeController(self):
        for model in self.controllermodellist:
            utl = UtilPhysicEthernetInterface()
            utl.configPhysicEthernetInterface(model.data)