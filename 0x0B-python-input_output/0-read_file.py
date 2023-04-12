#!/usr/bin/python3

"""0-read_file Module
Reads a text file
"""


def read_file(filename=""):
    with open(filename, 'r', encoding='UTF8') as a_file:
        print(a_file.read())
