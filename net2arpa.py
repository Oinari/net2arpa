import sys
import ipaddress

def help():
    print(sys.argv[0]+" generates reverse DNS zonefiles for a given subnet.")
    print("Usage "+sys.argv[0]+" [ipblock]")
    print("Example: "+sys.argv[0]+" 10.0.0.0/8")

if len(sys.argv) is not 2:
    help()
    sys.exit(1)

CurrentNet = ipaddress.ip_network(sys.argv[1])

SubnetList = CurrentNet.subnets(new_prefix=24)
print(*SubnetList, sep = "\n")

#for val in SubnetList:
#    SubnetHostsList = ipaddress.ip_network(val).network_address

#SubnetHostsList = ipaddress.ip_network('10.0.7.0/24').network_address
#print(*SubnetHostsList, sep = "\n")
