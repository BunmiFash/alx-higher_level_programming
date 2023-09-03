#!/usr/bin/python3
"""
A Python script that takes in a URL sends a request
to the passed URL and displays the body of
the response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as resp:
            response = resp.read()
            response = response.decode('utf-8')
            print(response)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
