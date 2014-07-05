#!/usr/bin/python

ipv6 = "FE80:0000:0000:0000:0101:A3EF:EE1E:1719"

# Exercise 1 - split ipv6 address
print "IPv6 address split\n"
ipv6_split = ipv6.split(':')
print ipv6_split

# Exercise 2 - re-join split ipv6 address
print "\nIPv6 address joined\n"
print ':'.join(ipv6_split)
