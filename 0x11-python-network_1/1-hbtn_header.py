#!/usr/bin/python3
"""
A python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print(resp.getheader('X-Request-Id'))
