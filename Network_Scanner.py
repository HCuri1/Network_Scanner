#!/usr/bin/env python

import ARP_Request

ip= str(input("IP address or Network to scan: "))
ARP_Request.request(ip)