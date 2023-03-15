#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_val = 0
        max_key = ""
        keys = a_dictionary.keys()
        for key in keys:
            if a_dictionary[key] > max_val:
                max_val = a_dictionary[key]
                max_key = key
        return max_key
    else:
        return None
