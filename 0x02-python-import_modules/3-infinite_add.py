#!/usr/bin/python3

import sys
if __name__ == "__main__":
    argv = sys.argv
    len_arg = len(argv)

    if (len_arg == 1):
        sum = int(0)
    else:
        sum = int(0)
        for i in range(1, len_arg):
            sum += int(argv[i])
    print(sum)
