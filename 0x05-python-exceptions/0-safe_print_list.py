#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for x in range(0, x):
            print("{}".format(my_list[x]), end="")
        print()
        return (x + 1)
    except IndexError:
        print()
        return x
