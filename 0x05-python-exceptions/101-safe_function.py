#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
        return res
    except BaseException as ex:
        print("Exception: {0}".format(ex), file=sys.stderr)
        return None
