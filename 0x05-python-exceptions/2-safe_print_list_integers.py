#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    idx = 0
    count = 0

    while idx < x:
        for i in my_list:
            try:
                print("{:d}".format(my_list[idx]), end='')
                count += 1
                break
            except ValueError:
                continue
            except TypeError:
                continue
        idx += 1
    print()
    return count
