#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    elif not first_name and not last_name:
        raise TypeError("function must have one argument")
    else:
        print("my name is {} {}".format(first_name, last_name))