#!/usr/bin/python3
"""
this is a Shebang used to make python script
"""


class MyList(list):
    """class named my list that inherite list object)"""
    def __init__(self):
        """initialize init method"""
        super().__init__()

    def print_sorted(self):
        """method to print sorted list"""
        s_list = sorted(self)
        print(s_list)
