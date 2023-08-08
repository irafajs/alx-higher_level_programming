#!/usr/bin/python3
def uppercase(s):
    output = ""
    for char in s:
        if 'a' <= char <= 'z':
            output += "{}".format(chr(ord(char) - ord('a') + ord('A')))
        else:
            output += "{}".format(char)
    print(output)
