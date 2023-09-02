#!/usr/bin/python3
"""
A python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        response = resp.read()
        print('Body response:')
        print('\t- type: ', response.__class__)
        print('\t- content: ', response)
        print('\t- utf8 content: ', response.decode('utf-8'))
