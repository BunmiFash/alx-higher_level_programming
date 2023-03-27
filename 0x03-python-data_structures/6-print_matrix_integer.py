#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    
    for row in matrix:
        last_idx = len(row) - 1
        for i in row:
            if i == row[-1]: 
                print("{:d}".format(i), end='')
            else:
                print("{:d}".format(i), end="")
        print()
