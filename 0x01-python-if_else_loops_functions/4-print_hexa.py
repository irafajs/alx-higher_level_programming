#!/usr/bin/python3
for decimal in range(0, 99):
    hexa = "0x{:x}".format(decimal)
    print("{} = {}".format(decimal, hexa))
