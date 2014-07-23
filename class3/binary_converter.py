#!/usr/bin/python

import sys

if len(sys.argv) == 2:
    ip_addr = sys.argv.pop()
    split_addr = ip_addr.split(".")
    for index, octet in enumerate(split_addr):
       split_addr[index] = bin(int(octet))
    print "%20s %20s %20s %20s" % ("first_octet", "second_octet", "third_octet", "fourth_octet")
    print "".join(split_addr]
