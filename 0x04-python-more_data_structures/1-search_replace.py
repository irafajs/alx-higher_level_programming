#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search < 0 or search >= len(my_list) or replace == None:
        return my_list.copy()
    new_l = my_list.copy()
    new_l[search - 1] = replace
    return new_l
