#!/usr/bin/python3

import sys

argv = sys.argv
arg_len = len(argv)
count = 1

if (arg_len == 1):
    print('0 arguments.')
elif (arg_len == 2):
    print("{:d} argument:".format(1))
    print("{:d}: {}".format(1, argv[1]))

else:
    print("{:d} arguments:".format(arg_len - 1))
    for i in range(1, arg_len):
        print("{:d}: {}".format(i, argv[i]))
