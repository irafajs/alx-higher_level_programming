#!/usr/bin/python3
stri = "'LockedClass' object has no attribute"
class LockedClass:
    def __setattr__(self, name, value):
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError("{}'{}'".format(stri, name))
