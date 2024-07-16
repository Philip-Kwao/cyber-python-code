#!/usr/bin/python3
import random, subprocess

# Ansi Color Codes
RED = "\033[0;31m"
GREEN = "\033[0;32m"
LIGHT_WHITE = "\033[1;37m"

# Create random Mac address
random_addr = [0x00, 0x5a, 0x3d, random.randint(0x00,0x7f), random.randint(0x00, 0xff), random.randint(0x00,0xff)]
# print(random_addr)

mac_addr = ":".join(map(lambda x: "%02x" %x, random_addr))


# Change Mac Address
print(RED, "Old MAC Address: ", GREEN)
subprocess.call(["ip", "link", "show", "eth0"])                        #Display Old Mac Address
print(LIGHT_WHITE)
subprocess.call(["ifdown", "eth0"])                                    #Turn off LAN
subprocess.call(["ip", "link", "set", "eth0", "down"])                 #Turn off NIC
subprocess.call(["ip", "link", "set", "eth0", "address", mac_addr])    #Replace Old Mac Address with New Mac Address
subprocess.call(["ip", "link", "set", "eth0", "up"])                   #Turn on NIC
print(RED, "New MAC Address: ", GREEN)
subprocess.call(["ip", "link", "show", "eth0"])                        #Display New Mac Address  
