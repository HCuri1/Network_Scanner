#!/usr/bin/env python

import ARP_Request
import argparse

parser=argparse.ArgumentParser()

parser.add_argument("-t", "--target", dest="ip", default="127.0.0.1", help="set IP address or network range (Model: x.x.x.x or x.x.x.x/x)")

options = parser.parse_args()

ip=str(options.ip).strip()

ARP_Request.request(ip)