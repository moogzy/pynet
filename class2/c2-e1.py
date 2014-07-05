#!/usr/bin/python

""" PyNet - Python for Network Engineers
    
    Class 2 - Exercise 1

    Author: Adrian Arumugam
    Date: 04/07/2014

"""

# Prompt user for IP network
ip_net = raw_input("Please input an IP network(/24): ")

# Split user input string of IP network
split_input  = ip_net.split(".")

# Take split_input list and slice it to remove the last octet
first_three_octets = split_input[:3]

# Append to list with 0 - to enforce assumption of /24 network
first_three_octets.append('0')

# Join the address back together again
actual_ip_net = ".".join(first_three_octets)

# Print out the /24 network for the user
print "Your /24 IP network is: %s" % actual_ip_net

# Convert the first octet of the IP network to its binary value
first_oct_bin = bin(int(first_three_octets[0]))

# Convert the first octet of the IP network to its hex value
first_oct_hex = hex(int(first_three_octets[0]))

# Print network number, first octet in binary and hex format with 20 character width columns
print "\n%20s %20s %20s" % ("NETWORK_NUMBER", "FIRST_OCTET_BINARY", "FIRST_OCTET_HEX")
print "\n%20s %20s %20s" % (actual_ip_net, first_oct_bin, first_oct_hex)
