#!/usr/bin/python3
#  Prints the number of and the list of its arguments
if __name__ == "__main__":
    import sys

    arg = sys.argv
    c = len(arg) - 1

    if c > 1:
        print("{} arguments:".format(c))
        for x in range(1, c + 1):
            print("{}: {}".format(x, arg[x]))

    elif c == 0:
        print("{} arguments.".format(c))

    else:
        print("{} argument:".format(c))
        print("{}: {}".format(c, arg[1]))
