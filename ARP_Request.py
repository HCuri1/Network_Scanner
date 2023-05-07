#!/usr/bin/env python

import scapy.all as scapy 

def request (ip):
    
    objectRequest = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    arpRequest = broadcast/objectRequest
    
    answeredList = scapy.srp(arpRequest, timeout=2, verbose=False)[0]
    
    exhibit(answeredList)

def exhibit (answeredList):
    
    print("IP\t\t\tMAC")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    
    for element in answeredList:
        
        print(element[1].psrc + "\t\t" + element[1].hwsrc)