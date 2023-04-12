#!/usr/bin/python3

"""Module 5-save_to_json_file
Converts a python object to a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """def save_to_json_file(my_obj, filename)"""

    with open(filename, 'w', encoding='UTF8') as a_file:
        return (json.dump(my_obj, a_file))
