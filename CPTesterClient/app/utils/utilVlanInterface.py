# Utility for Physical Ethernet interface
from app.model.modelTypes import *
import subprocess


class UtilVlanInterface():
    def configVlanInterface(self, param):
        print "Config Vlan Interface Enter"
        # print param["name"]
        # print "sh app/utils/tools/vlanInterface.sh",param["physicInterface"],param["vlanID"],param["hwAddr"],param["MTU"],param["ipAddr"],param["subnetMask"]
        # print ''.join(cmd)
        child = subprocess.Popen(["sh","app/utils/tools/vlanInterface.sh",param["physicInterface"],param["vlanID"],param["hwAddr"],param["MTU"],param["ipAddr"],param["subnetMask"]])
        # child = subprocess.Popen(["ifconfig","tap0"])
        child.wait()
        print "Parent process"