#!/usr/bin/env python3

import sys
import ipaddress
import re

def help():
    print(sys.argv[0]+" generates reverse DNS zonefiles for a given subnet.")
    print("Usage "+sys.argv[0]+" [ipblock]")
    print("Example: "+sys.argv[0]+" 10.0.0.0/8")

if len(sys.argv) != 2:
    help()
    sys.exit(1)

CurrentNet = ipaddress.ip_network(sys.argv[1])

SubnetList = CurrentNet.subnets(new_prefix=24)
SubnetList = list(SubnetList)
#print(*SubnetList, sep = "\n")

SubnetAddrList = [ipaddress.ip_network(addr).network_address for addr in SubnetList]
#print(*SubnetAddrList, sep = "\n")

ArpaAddrList = [ipaddress.ip_address(addr).reverse_pointer for addr in SubnetAddrList]
ArpaAddrList = [re.sub('^0.', '', addr) for addr in ArpaAddrList]
print(*ArpaAddrList, sep = "\n")

#>>> ipaddress.ip_network('10.0.7.0/24').network_address
#IPv4Address('10.0.7.0')

#>>> ipaddress.ip_address("1.1.1.0").reverse_pointer
#'0.1.1.1.in-addr.arpa'
