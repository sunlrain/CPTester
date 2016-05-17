#!/bin/bash

# vlanInterface.sh tap0 100 0019cb100001 1500 192.168.1.33 255.255.255.0

echo "vlanInterface.sh Enter"

if [ -z $1 ] || [ -z $2 ] || [ -z $3 ] || [ -z $4 ] || [ -z $5 ] || [ -z $6 ];
then
    echo "Usage: vlanInterface.sh tap0 100 0019cb100001 1500 192.168.1.33 255.255.255.0"
    exit
fi

IFNAME=$1
VLANID=$2
MACADDR=$3
MTU=$4
IPADDR=$5
NETMASK=$6

NULLSTRING="NULL"

## Check if the physic interface exists
ifconfig $IFNAME > /dev/null 2>&1
if [ $? -ne 0 ];
then
    echo "====Physical Ethernet Interface doesn't exist, please check!"
    exit
fi

#check whether the vlan interface exist
ifconfig $IFNAME.$VLANID > /dev/null 2>&1
if [ $? -eq 0 ]; then
	echo "=====Error: $IFNAME.$VLANID already exist, please check!"
else
    echo "vconfig interface: vconfig add $IFNAME $VLANID"
    vconfig add $IFNAME $VLANID
fi
#echo $IPADDR
#echo $NETMASK
#echo $VLANID
#

if [ ${IPADDR} = ${NULLSTRING} ] || [ ${NETMASK} = ${NULLSTRING} ];
then
    echo "vconfig without IP Address: ifconfig $IFNAME.$VLANID hw ether $MACADDR mtu $MTU"
    ifconfig $IFNAME.$VLANID hw ether $MACADDR mtu $MTU
else
    echo "vconfig with IP Address: ifconfig $IFNAME.$VLANID hw ether $MACADDR mtu $MTU $IPADDR netmask $NETMASK"
    ifconfig $IFNAME.$VLANID hw ether $MACADDR mtu $MTU $IPADDR netmask $NETMASK
fi

ifconfig $IFNAME.$VLANID up


