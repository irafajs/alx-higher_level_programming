#!/usr/bin/python3
l_case = 'a'
a = ""
for l_case in range(122, 97):
    a -= "{}".format(chr(l_case))
print(a, end="")
