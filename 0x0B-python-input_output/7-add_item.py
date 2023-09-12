#!/usr/bin/python3
"""
Shebang to create a python script
"""


import sys


imp_f5 = __import__('5-save_to_json_file').save_to_json_file
imp_f6 = __import__('6-load_from_json_file').load_from_json_file

try:
    items = imp_f6("add_item.json")
except FileNotFoundError:
    items = []

for arg in sys.argv[1:]:
    items.append(arg)

imp_f5(items, "add_item.json")
