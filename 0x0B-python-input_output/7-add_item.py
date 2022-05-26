#!/usr/bin/python3
""" script that adds arguments to a python list and saven them """
import os.path
from sys import argv
""" sys allows me to receive the string to add in the file from the cl
for accessing the filesystem os.path """


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

p_list = []
if os.path.exists("add_item.json"):
    p_list = load_from_json_file("add_item.json")
save_to_json_file(p_list + argv[1:], "add_item.json")
