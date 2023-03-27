#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    y = 0
    count = 0
    try:
        while (y < x):
            for i in my_list:
                print(my_list[y], end='')
                break
            y += 1
        print()
        return x
    except IndexError:
        for i in my_list:
            count += 1
        print()
        return count
