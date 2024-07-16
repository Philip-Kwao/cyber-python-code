#!/usr/bin/python3
import argparse
import ipaddress
import sys
import time
import scapy.all as scapy

#Construct Argument

parser = argparse.ArgumentParser(description = "This script is going to trace the route of the specified IP Address")
parser.add_argument('-t', '--target_ip_address', help="This is the targeted IP Address")
parser.add_argument('-m', '--max_hop_limit', type=int, help="This is the Maximum Hop Limit")

# Get Argument
args=parser.parse_args()
target_ip_address=args.target_ip_address
max_hop_limit=args.max_hop_limit
print(target_ip_address, max_hop_limit)


#Validate IP Address
def is_valid_ip(address):
    try:
        ipaddress.ip_address(address)
        return True
    except ValueError:
        return False
if(is_valid_ip(target_ip_address)==False):
    print("Invalid Input")
    sys.exit(1)

# TTL Initialization
TTL=1
print("Trace Routing has begun ...")
T1=time.time()

while(TTL<= max_hop_limit):
    ICMP_PKT=scapy.IP(dst=target_ip_address, ttl=TTL)/scapy.ICMP()
    ans=scapy.sr1(ICMP_PKT, timeout=3, retry=1, verbose=False)

    ## Valid response is received
    if(isinstance(ans,type(None))==False):
        ## ICMP TTL expired
        if(ans[1].type==11 and ans[1].code==0):
            print("router", ans[0].src, " | TTL",TTL)
            TTL+=1
        if(ans[1].type==0):
            print("router", target_ip_address, " | TTL",TTL)
    ##No response
    else:
        print("Unknown router | TTL",TTL)
        TTL +=1

T2=time.time()
print("IP tracerouting done in ", T2-T1,"seconds ...")
