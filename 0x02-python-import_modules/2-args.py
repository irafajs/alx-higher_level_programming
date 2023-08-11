#!/usr/bin/python3
import sys


if __name__ == "__main__":
    count = len(sys.argv)
    if count == 1:
        print("{} arguments.".format(count - 1))
    elif count == 2:
        print("{} argument:".format(count - 1))
    else:
        print("{} arguments:".format(count - 1))
    for a_count in range(1, count):
        print("{}: {}".format(a_count, sys.argv[a_count]))
