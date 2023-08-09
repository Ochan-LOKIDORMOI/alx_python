#!/usr/bin/python3
"""I documented you"""

from urllib.request import urlopen
import sys

if __name__ == '__main__':
    with urlopen(sys.argv[1]) as res:
        header = res.info()
        print(header["X-Request-Id"])
