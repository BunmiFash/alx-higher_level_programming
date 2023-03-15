#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list == 0):
        return 0
    add = 0
    div = 0
    for sub in my_list:
        add += (sub[0] * sub[1])
        div += sub[1]
    return (add / div)
