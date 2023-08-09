#!/usr/bin/python3

"""This script takes in a URL, sends a request to the URL and displays
the value of X-Request-Id varialble found in the header
of the response"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))