#!/usr/bin/env python

import scapy.all as scapy 

def request (ip):
    
    objectRequest = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    
    arpRequest = objectRequest/broadcast
    
    answeredList = scapy.srp(arpRequest, timeot=1)[0]
    
    exhibit(answeredList)

def exhibit (answeredList):
    
    for element in answeredList:
        
        print(element)