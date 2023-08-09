#!/usr/bin/env python3
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id is not None:
        print(x_request_id)
    else:
        print("X-Request-Id not found in the response headers.")
except requests.ConnectionError:
    print("School")
except requests.RequestException as e:
    print("An error occurred:", e)