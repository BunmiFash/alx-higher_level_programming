#!/usr/bin/python3

"""0-read_file Module
Reads a text file
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding='UTF8') as a_file:
        print(a_file.read())
