#!/usr/bin/python

""" PyNet - Python for Network Engineers

    Class 3 - Exercise 3

    Author: Adrian Arumugam
    Date: 23/07/2014

"""

# 'show ip bgp' output in a list for processing
bgp_entries=["*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i","*  1.1.1.0/24     157.130.10.233        0 701 1299 15169 i","*  1.1.42.0/24    157.130.10.233        0 701 9505 17408 2.1465 i", "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"]

# Print header for output
print "%-20s %-20s" % ("ip_prefix", "as_path")

# Process each index in bgp_entries list for for loop.
#
# Split each entry on spaces " ".
# Create index for AS701 and store in find_index.
# Print the output via format string.
for index, output in enumerate(bgp_entries):
 bgp_entries[index] = output.split(" ")
 find_index = bgp_entries[index].index("701")
 print "%-20s %-20s" % (bgp_entries[index][2], bgp_entries[index][find_index:-1]) 
