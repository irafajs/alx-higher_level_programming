#!/usr/bin/python3
"""__doc__"""


def text_indentation(text):
    """function to indent to a new line"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    punctuation_chars = ['.', '?', ':']
    result = []
    line = ""
    for char in text:
        line += char
        if char in punctuation_chars:
            result.append(line.strip())
            result.append('\n\n')
            line = ""
    if line:
        result.append(line.strip())
    print("".join(result))
