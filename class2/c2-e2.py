#!/usr/bin/python

""" PyNet - Python for Network Engineers
    
    Class 2 - Exercise 2

    Author: Adrian Arumugam
    Date: 04/07/2014

"""

# Prompt user for IP address in dotted decimal format
ip_addr = raw_input("Please enter an IP address in dotted decimal format: ")

# Split IP address for handling
split_addr = ip_addr.split(".")

# Assign each octet to a variable and convert to binary value
octet1 = bin(int(split_addr[0]))
octet2 = bin(int(split_addr[1]))
octet3 = bin(int(split_addr[2]))
octet4 = bin(int(split_addr[3]))

# Print table to show binary value of each octet in IP address
print "%20s %20s %20s %20s" % ("first_octet", "second_octet", "third_octet", "fourth_octet")
print "\n%20s %20s %20s %20s" % (octet1, octet2, octet3, octet4)
