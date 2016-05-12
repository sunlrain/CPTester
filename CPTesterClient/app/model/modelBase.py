# Definition of base model

class modelBase:
    def __init__(self, modelData, modelKeys):
        self.keys = modelKeys
        self.data = modelData
        # print modelType
        # if (modelType == "brInterfaces"):
        #     print("bridge Interfaces init")
        #     self.keys = ["bridgeInterfaces","name", "hwAddr", "MTU", "ipAddr", "subnetMask", "gateway"]
        # elif (modelType == "comInterfaces"):
        #     print("Com Interfaces init")
        #     self.keys = ["ipAddr","port"]
        # elif (modelType == "physicEthernetInterfaces"):
        #     print("Physic Ethernet Interfaces init")
        #     self.keys = ["name", "hwAddr", "MTU", "ipAddr", "subnetMask", "gateway"]
        # elif (modelType == "vlanInterfaces"):
        #     print("vlan Interfaces init")
        #     self.keys = ["physicInterface", "vlanID", "name", "hwAddr", "MTU", "ipAddr", "subnetMask", "gateway"]
        # elif (modelType == "containerDNSMASQ"):
        #     print("container DNSMASQ init")
        #     self.keys = ["type", "inetrfaceName", "hwAddr", "ipAddr", "subnetMask", "gateway", "dhcpConfig", "dhcpPool", "dnsConfig"]
        # else:
        #     print("ERROR: Base Model Init - Not support model type")

    # def __init__(self, parm):
    #     self.status = "init"
    #     print("Base Model Init with parm", type(parm))

    # def initModel(self, modelData):
    #     self.data = modelData

    def printModel(self):
        print " "
        print "----------Print Model Start"
        for key in self.keys:
            print key, ":", self.data[key]
        print "----------Print Model End"