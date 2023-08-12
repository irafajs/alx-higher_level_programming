#!/usr/bin/python3
def no_c(my_string):
    noc_s = ""
    for item in range(len(my_string)):
        if my_string[item] != 'c' and my_string[item] != 'C':
            noc_s = noc_s + my_string[item]
    return noc_s
