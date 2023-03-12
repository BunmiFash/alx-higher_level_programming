#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul
    argv = sys.argv
    arg_len = len(argv)
    operator = ['*', '+', '-', '/']

    if (arg_len != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    elif argv[2] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    else:
        a = int(argv[1])
        operator = argv[2]
        b = int(argv[3])
        if (operator == '+'):
            print("{:d} {} {:d} = {:d}".format(a, operator, b, add(a, b)))

        elif (operator == '-'):
            print("{:d} {} {:d} = {:d}".format(a, operator, b, sub(a, b)))

        elif (operator == '*'):
            print("{:d} {} {:d} = {:d}".format(a, operator, b, mul(a, b)))

        else:
            print("{:d} {} {:d} = {:d}".format(a, operator, b, div(a, b)))
