#!/usr/bin/python3
for decimal in range(0, 99):
    hexa = "0x{:X}".format(decimal)
    print("{:2} = {:4}".format(decimal, hexa))
