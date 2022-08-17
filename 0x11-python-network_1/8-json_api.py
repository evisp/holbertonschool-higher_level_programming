#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":

    q = ""
    if len(argv) > 1:
        q = argv[1]
    letter = {'q': q}
    req = requests.post('http://0.0.0.0:5000/search_user', letter)
    try:
        get_json = req.json()
        if get_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(get_json.get('id'), get_json.get('name')))
    except:
            print("Not a valid JSON")
