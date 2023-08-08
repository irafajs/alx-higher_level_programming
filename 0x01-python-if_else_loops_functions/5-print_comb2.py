#!/usr/bin/python3
output = ""
for i in range(100):
    if i == 99:
        output += "{:02}".format(i)
    else:
        output += "{:02}, ".format(i)
print(output)
