#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    add = 0
    div = 0
    for sub in my_list:
        score = sub[0]
        weight = sub[1]
        mult = score * weight
        add += mult
        div += weight
    return (add / div)
