# Utility for Physical Ethernet interface
from app.model.modelTypes import *
import subprocess


class UtilPhysicEthernetInterface():
    def configPhysicEthernetInterface(self, param):
        print "Config Physical Ethernet Interface Enter"
        # print param["name"]
        child = subprocess.Popen(["sh","app/utils/tools/physicEthernetInterface.sh",param["name"],param["hwAddr"],param["MTU"],param["ipAddr"],param["subnetMask"]])
        # child = subprocess.Popen(["ifconfig","tap0"])
        child.wait()
        print "Parent process"