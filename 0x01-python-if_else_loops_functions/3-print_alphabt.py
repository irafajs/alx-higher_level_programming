#!/usr/bin/python3
a = ""
for l_case in range(97, 123):
    char = chr(l_case)
    if char != 'e' and char != 'q':
        a += "{}".format(char)
print(a, end="")
