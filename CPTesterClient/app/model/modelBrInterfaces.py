# Model of bridge interfaces
from modelBase import modelBase


class modelBrInterfaces(modelBase):
    def __init__(self):
        print("Bridge Interfaces init")
        self.keys = ["bridgeInterfaces","name", "hwAddr", "MTU", "ipAddr", "subnetMask", "gateway"]

    # def __init__(self, parm):
    #     self.status = 0  # Init status
    #     self.errorCode = ""  # Set error code to NULL
    #     print("Bridge Interfaces init with parm", type(parm))


    # def initBridgeInterface(self, interface):
    #     print("Init Bridge Interface Start")
    #     print type(interface)
    #     for(k,v) in interface.items():
    #         print type(k),"=",k, type(v)
    #     self.bridgeInterfaces = interface["bridgeInterfaces"]
    #     self.name = interface["name"]
    #     self.hwAddr = interface["hwAddr"]
    #     self.MTU = interface["MTU"]
    #     self.ipAddr = interface["ipAddr"]
    #     self.subnetMask = interface["subnetMask"]
    #     self.gateway = interface["gateway"]
    #     print("Init Bridge Interface End")

    # def printBridgeInterface(self):
    #     print("Print Bridge Interface")
    #     print "bridgeInterfaces:", self.bridgeInterfaces
    #     print "name:", self.name
    #     print "hwAddr:", self.hwAddr
    #     print "MTU:", self.MTU
    #     print "ipAddr:", self.ipAddr
    #     print "subnetMask:", self.subnetMask
    #     print "gateway:", self.gateway



