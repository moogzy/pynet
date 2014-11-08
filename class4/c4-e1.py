#!/usr/bin/python

""" Pynet - Python for Network Engineers

    Class 4 - Exercise 1
    
    Check validity of an IP address from input.
    
    1. IP address must have 4 octets
    2. First octet must be 1 - 223
    3. First octet can't be 127
    4. IP address cannot be in the 169.254.x.x block
    5. Final three octets must be 0 - 255
    
    Continue to prompt the user for input until a 
    valid IP address has been entered.
    
    Author: Adrian Arumugam
    Date: 08/11/2014
"""

status = "invalid"
valid_ip = False
arg_missing = "Please provide an argument - %s <ip_address>"
statement = "IP address: %s is %s"

# Assume valid_ip is always false until user enters a valid IP address
while valid_ip == False:

    # Handle input and split on "." to verify that 4 octets exist
    # if there isn't 4 octets then return to the input prompt.
    input = raw_input("Enter an IP address: ")
    ip_addr = input.split(".")
    if len(ip_addr) != 4:
        print statement % (input, status) + " must have four octets!\n"
        continue

    # If 4 octets exist then lets verify them. Convert them via typecase
    # to an integer for comparison. If the last octet is empty then we
    # handle this via an exception and return to the input prompt.
    else:
        for index, octet in enumerate(ip_addr):
            try:
                ip_addr[index] = int(octet)
            except ValueError:
                print statement % (input, status) + " no empty octets allowed!\n"
    if ip_addr[3] == "":
        continue

    # Assign a name to each of the octets in ip_addr variable.
    first_oct, second_oct, third_oct, fourth_oct = ip_addr

    # Validate first and second octet to ensure not in 169.254.x.x block
    if first_oct == 169 and second_oct == 254:
        print statement % (input, status) + " cannot be in 169.254.x.x block!\n"
        continue
    
    # Ensure the first octet is not 127
    if first_oct == 127:
        print statement % (input, status) + " first octet cannot be 127!\n"
        continue
    
    # Validate first octet to ensure it is > 0 and  < 223:
    if (first_oct > 0) and (first_oct <= 223):

        # Validate the second, third and fourth octet to ensure they are
        # >= 0 and <= 255. If this is true then change variable assignment in
        # preparation of exiting the loop.
        if (second_oct >= 0) and (second_oct <= 255):
            if (third_oct >= 0) and (third_oct <= 255):
                if (fourth_oct >= 0) and (fourth_oct <= 255):
                    valid_ip = True
                    status = "valid"

    # If the first octet is not valid then advise the user.
    else:
        print statement % (input, status) + " first octet must be > 0 and <= 223!\n"
        continue
    
    # If all octets were valid then valid_ip will be "True", print statement and continue
    # loop will no longer execute due to false comparison.
    if valid_ip == True:
        print statement % (input, status) + "\n"
        continue

    # If the second, third or fourth octet was invalid then advise the user and return to the
    # input prompt.
    else:
        print statement % (input, status) + " 2nd, 3rd and 4th octets must be >= 0 and <= 255!\n"
        continue
