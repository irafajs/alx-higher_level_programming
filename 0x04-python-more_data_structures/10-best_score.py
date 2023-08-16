#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        h_value = max(a_dictionary, key=a_dictionary.get)
        return h_value
    else:
        return None
