# Controller of Bridge Interfaces

from app.controller.controllerBase import *


class ControllerBrInterfaces(controllerBase):
    def sayhello(self):
        print "Hello"

    def executeController(self):
        self.sayhello()
