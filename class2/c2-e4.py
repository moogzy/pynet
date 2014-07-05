#!/usr/bin/python

""" PyNet - Python for Network Engineers
    
    Class 2 - Exercise 4

    Author: Adrian Arumugam
    Date: 04/07/2014

"""

# String variable from Cisco.
cisco_ios = "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.0(1)M4, RELEASE SOFTWARE (fc1)"

# Split the string to create four sections store in a list.
split_str = cisco_ios.split(",")

# Access index 2 of the list of strings, strip leading white space then split on spaces.
split_version = split_str[2].strip().split(" ")

# Assign index one to variable as this should now be the IOS Version we are after.
ios_version = split_version[1]

# Print the IOS version.
print "The Cisco IOS version is %s " % (ios_version)
