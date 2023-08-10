#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
and displays the body of the response
"""
if __name__ == "__main__":
    import sys
    import requests
    
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)
        
    url = sys.argv[1]
    r = requests.get(url)
    
    if r.status_code >= 400:
        print("Error code:", r.status_code)
        sys.exit(1)
    else:
        print(r.text)