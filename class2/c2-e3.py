#!/usr/bin/python

""" PyNet - Python for Network Engineers
    
    Class 2 - Exercise 3

    Author: Adrian Arumugam
    Date: 04/07/2014

"""

# BGP output variables
entry1 = "*  1.0.192.0/18   157.130.10.233        0 701 38040 9737 i"
entry2 = "*  1.1.1.0/24     157.130.10.233        0 701 1299 15169 i"
entry3 = "*  1.1.42.0/24    157.130.10.233        0 701 9505 17408 2.1465 i"
entry4 = "*  1.0.192.0/19   157.130.10.233        0 701 6762 6762 6762 6762 38040 9737 i"

# Split each string on spaces
one_split = entry1.split(" ")
two_split = entry2.split(" ")
three_split = entry3.split(" ")
four_split = entry4.split(" ")

# Create index of AS701 to be used as slice value in output for AS path
index1 = one_split.index("701")
index2 = two_split.index("701")
index3 = three_split.index("701")
index4 = four_split.index("701")


# Print IP prefix and AS path via list slicing with left align width 20 column
print "%-20s %-20s" % ("ip_prefix", "as_path")
print "%-20s %-20s" % (one_split[2], one_split[index1:-1])
print "%-20s %-20s" % (two_split[2], two_split[index2:-1])
print "%-20s %-20s" % (three_split[2], three_split[index3:-1])
print "%-20s %-20s" % (four_split[2], four_split[index4:-1])
