#!/usr/bin/env python

import scapy.all as scapy 

def request (ip):
    
    objectRequest = scapy.ARP(pdst=ip)