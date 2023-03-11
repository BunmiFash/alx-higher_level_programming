#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    last_idx = len(my_list) - 1
    if (idx < 0) or (idx > last_idx):
        return my_list
    new = []
    for i in my_list:
        new.append(i)
    new[idx] = element
    return new
