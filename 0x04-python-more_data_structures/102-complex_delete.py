#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    values = list(a_dictionary.values())
    keys = list(a_dictionary.keys())
    for x in range(len(values)):
        if values[x] == value:
            del a_dictionary[keys[x]]
    return a_dictionary
