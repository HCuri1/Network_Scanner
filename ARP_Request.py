#!/usr/bin/env python

import scapy.all as scapy 

def request (ip):
    
    objectRequest = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    arpRequest = broadcast/objectRequest
    
    answeredList = scapy.srp(arpRequest, timeout=2)[0]
    
    exhibit(answeredList)

def exhibit (answeredList):
    
    for element in answeredList:
        
        print("IP: ", element[1].psrc)
        print("IP: ", element[1].hwsrc)
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*")