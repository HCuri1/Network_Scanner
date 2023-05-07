#!/usr/bin/env python

import scapy.all as scapy 

def request (ip):
    
    scapy.arping(ip)