#!/usr/bin/python

""" PyNet - Python for Network Engineers

    Class 3 - Exercise 1

    Author: Adrian Arumugam
    Date 23/07/2014

"""

import sys

# Verify arguments passed to command line
if len(sys.argv) == 2:
    
    # Pop off the IP address and assign to variable
    ip_addr = sys.argv.pop()

    # Split the IP address on the decimal for further processing
    split_addr = ip_addr.split(".")

    # Iterate over the split ip address list
    #
    # Convert each list entry into binary equivalent.
    # Strip leading "0b" from the binary value.
    # Enter a while loop to pad each binary value with leading "0s"
    # until binary value is eight digits in length.
    for index, octet in enumerate(split_addr):
       split_addr[index] = bin(int(octet))
       split_addr[index] = split_addr[index].lstrip("0b")
       while len(split_addr[index]) <= 7:
          split_addr[index] = "".join(("0", split_addr[index]))

    # Print out results using format strings.
    print "%-20s %-s" % ("IP address", "Binary")
    print "%-20s %-s.%-s.%s.%s" % (ip_addr, split_addr[0], split_addr[1], split_addr[2], split_addr[3])
