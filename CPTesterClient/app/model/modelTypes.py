modelTypes = {
    'brInterfaces':["bridgeInterfaces","name", "hwAddr", "MTU", "ipAddr", "subnetMask", "gateway"],
    'comInterfaces':["ipAddr","port"],
    'physicEthernetInterfaces':["name", "hwAddr", "MTU", "ipAddr", "subnetMask", "gateway"],
    'vlanInterfaces':["physicInterface", "vlanID", "name", "hwAddr", "MTU", "ipAddr", "subnetMask", "gateway"],
    'containerDNSMASQ':["type", "inetrfaceName", "hwAddr", "ipAddr", "subnetMask", "gateway", "dhcpConfig", "dhcpPool", "dnsConfig"]
}
