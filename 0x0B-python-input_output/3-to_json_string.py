#!/usr/bin/python3

"""Module 3-to_json_string
Converts a python object to a JSON string
"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""

    return (json.dumps(my_obj))
