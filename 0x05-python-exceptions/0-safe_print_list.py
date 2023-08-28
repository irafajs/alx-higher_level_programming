#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for item in range(x):
            print("{}".format(my_list[item]), end="")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count
