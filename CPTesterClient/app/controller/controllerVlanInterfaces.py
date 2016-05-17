# Controller for Vlan interfaces
from app.controller.controllerBase import *
from app.utils.utilVlanInterface import *


class ControllerVlanInterfaces(controllerBase):
    def sayhello(self):
        print "Hello"

    def executeController(self):
        print "Execute Vlan Interface Controller Enter"

        for model in self.controllermodellist:
            # print model.data
            utl = UtilVlanInterface()
            utl.configVlanInterface(model.data)