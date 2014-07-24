#!/usr/bin/python

""" Pynet - Python for Network Engineers

    Class 3 - Exercise 4
    
    Check validity of an IP address passed via argument.
    
    1. IP address must have 4 octets
    2. First octet must be 1 - 223
    3. First octet can't be 127
    4. IP address cannot be in the 169.254.x.x block
    5. Final three octets must be 0 - 255
    
    Author: Adrian Arumugam
    Date: 24/07/2014
"""

import sys

# Check for argument, exit if none.
if len(sys.argv) != 2:
    sys.exit("\n\nUsage: %s <ip_address>\n" % sys.argv[0])

# Pop off IP address from list
ip_addr = sys.argv.pop()

# Split IP based on decimals
octets = ip_addr.split(".")

# Initialize variables for use throughout the script
status = "valid"
valid_ip = True
statement = "\n\nIP address: %s is %s\n"

# Validate for 4 octets, exit if less than 4    
if len(octets) != 4:
    sys.exit("\n\n%s is Invalid - Address must have 4 octets!" % ip_addr)

# Typecase the list entries to integers for comparisons
for index, octet in enumerate(octets):
    
    # Handle when last octet is empty(e.g '1.1.1.' via exception.
    # Exit script if this incorrect input is received.
    try:
       octets[index] = int(octet)
    except ValueError:
        status = "invalid"
        sys.exit(statement % (ip_addr, status))

# Map variables to all elements in octets list.
first_octet, second_octet, third_octet, fourth_octet = octets

# Validate first octet according to conditions.
if first_octet < 1:
    valid_ip = False
elif first_octet > 223:
    valid_ip = False
elif first_octet == 127:
    valid_ip = False

# Validate first and second octet to ensure not in 169.254.x.x block
if first_octet == 169 and second_octet == 254:
    valid_ip = False

# Validate last three octets to ensure 0 - 255
for octet in (second_octet, third_octet, fourth_octet):
    if (octet < 0) or (octet > 255):
        valid_ip = False

# Perform comparion for True\False and print respective statement.
if valid_ip:
    print statement % (ip_addr, status)
else:
    status = "invalid"
    sys.exit(statement % (ip_addr, status))

                    
 
