#!/usr/bin/python3
def results(argv):
    mx = len(argv) - 1
    if mx == 0:
        print("{:d}".format(mx))
        return
    else:
        y = 1
        res = 0
        while y <= mx:
            res += int(argv[y])
            y += 1
        print("{:d}".format(res))


if __name__ == "__main__":
    import sys
    results(sys.argv)
