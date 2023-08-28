#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for item in range(x):
            s_item = my_list[item]
            if not isinstance(s_item, int):
                continue
            print("{:d}".format(s_item), end="")
            count += 1
        print()
        return count
    except ValueError:
        print()
        return count
