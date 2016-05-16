#!/bin/bash

# physicEthernetInterface.sh tap0 0019cb100001 1500 192.168.1.33 255.255.255.0

if [ -z $1 ] || [ -z $2 ] || [ -z $3 ] ;
then
    echo "Usage: physicEthernetInterface.sh tap0 0019cb100001 1500 192.168.1.33 255.255.255.0"
    exit
fi

IFNAME=$1
MACADDR=$2
MTU=$3
IPADDR=$4
NETMASK=$5

NULLSTRING="NULL"

## Check if the physic interface exists
ifconfig $IFNAME > /dev/null 2>&1
if [ $? -ne 0 ];
then
    echo "====Physical Ethernet Interface doesn't exist, please check!"
    exit
fi

#echo $IPADDR
#echo $NETMASK
#
if [ ${IPADDR} = ${NULLSTRING} ] || [ ${NETMASK} = ${NULLSTRING} ];
then
#    echo "Print without IP Address"
    ifconfig $IFNAME hw ether $MACADDR mtu $MTU
else
#    echo "Print with IP Address"
    ifconfig $IFNAME hw ether $MACADDR mtu $MTU $IPADDR netmask $NETMASK
fi


