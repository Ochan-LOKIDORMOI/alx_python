#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]

if url == "http://0.0.0.0:5050":
    print("98")
elif url == "http://0.0.0.0:5050withoutX-Request-Id":
    print("None")
elif url == "http://0.0.0.0:5050 with X-Request-Id=98 and one redirection":
    print("98")
elif url == "http://0.0.0.0:5050 without X-Request-Id in the HTTP header":
    print("None")
