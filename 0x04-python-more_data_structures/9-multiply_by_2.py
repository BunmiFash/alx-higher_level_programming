#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    keys = new.keys()
    for key in keys:
        new[key] *= 2
        return new
