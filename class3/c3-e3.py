#!/usr/bin/python

""" PyNet - Python for Network Engineers

    Class 3 - Exercise 3
    
    Author: Adrian Arumugam
    Date: 23/07/2014

"""

# Import pprint to for cleaner out of list of tuples.
import pprint

# Show IP interfaces brief output.
show_ip_int_brief = '''
Interface       IP-Address      OK?     Method      Status     Protocol
FastEthernet0   unassigned      YES     unset       up         up
FastEthernet1   unassigned      YES     unset       up         up
FastEthernet2   unassigned      YES     unset       down       down
FastEthernet3   unassigned      YES     unset       up         up
FastEthernet4   6.9.4.10        YES     NVRAM       up         up
NVI0            6.9.4.10        YES     unset       up         up
Tunnel1         16.25.253.2     YES     NVRAM       up         down
Tunnel2         16.25.253.6     YES     NVRAM       up         down
Vlan1           unassigned      YES     NVRAM       down       down
Vlan10          10.220.88.1     YES     NVRAM       up         up
Vlan20          192.168.0.1     YES     NVRAM       down       down
Vlan100         10.220.84.1     YES     NVRAM       up         up
'''

# Split output based on new lines and create list
sh_ip_lines = show_ip_int_brief.split("\n")

# Initialize list for ability to .append later
sh_ip_list = []

# Iterate through each line in the list
for line in sh_ip_lines:

    # If 'Interface' exists then ignore, this skips the first line
    if 'Interface' in line:
        continue
    
    # Split line into words.
    line_split = line.split()
    
    # Filter out lines that don't have the expected number of fields. 
    if len(line_split) == 6:

        # Map variables given to the fields in the line_split list
        interface, ip_addr, state, method, status, protocol = line_split
        
        # If 'status' is 'up' and 'protocol' is 'up' for the line then we want to append
        # this interface, ip_addr, status and protocol to 'sh_ip_list'.
        if (status == 'up') and (protocol == 'up'):
            sh_ip_list.append((interface, ip_addr, status, protocol)) 

# Print new lines and use pprint to neaten up the list of tuples output for sh_ip_list
print "\n"
pprint.pprint(sh_ip_list)
print "\n"

