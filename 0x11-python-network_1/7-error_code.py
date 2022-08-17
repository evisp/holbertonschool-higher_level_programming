#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays
the body of the response.
If the HTTP status code is greater than or equal to 400,
print: Error code: followed by the value of the HTTP status code
packages requests and sys
"""

import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    status = req.status_code
    if status >= 400:
        print("Error code: {}".format(status))
    else:
        print(req.text)
