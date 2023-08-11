#!/usr/bin/python3
import sys


if __name__ == "__main__":
    count = len(sys.argv)
    sum = 0
    for a_count in range(1, count):
        sum += int(sys.argv[a_count])
    print("{}".format(sum))
