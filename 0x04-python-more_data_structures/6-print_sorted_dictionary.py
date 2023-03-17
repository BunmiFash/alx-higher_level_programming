#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(a_dictionary.keys())
    values = sorted(a_dictionary.values())
    newKeys = []
    if (len(a_dictionary) == 0):
        print("a_dictionary = {}")
    for i in keys:
        i = i.lower()
        newKeys.append(i)
    newKeys = sorted(newKeys)

    for key, values in zip(newKeys, values):
        print("{} : {}".format(key, values))
