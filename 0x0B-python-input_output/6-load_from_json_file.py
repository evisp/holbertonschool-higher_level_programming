#!/usr/bin/python3

"""Defines a string-to-JSON function."""
import json

def load_from_json_file(filename):
    """ function definition """
    with open(filename) as file:
        json.load(file)
