#!/usr/bin/python3

"""Module 6-load_from_json_file
Creates a python Object from a JSON file
"""

import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""

    with open(filename, encoding="UTF8") as a_file:
        return (json.load(a_file))
