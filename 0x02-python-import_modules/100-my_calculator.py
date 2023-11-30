#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import addition, substract, multiply, divide
    argc = len(argv)
    if argc != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    executes = {
        '+': addition,
        '-': substract,
        '*': multiply,
        '/': divide
    }
    if argv[2] in executes:
        res1 = int(argv[1])
        res2 = int(argv[3])
        res = executes[argv[2]]
        last = res(res1, res2)
        print('{:d} {:s} {:d} = {:d}'.format(res1, argv[2], res2, last))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)
