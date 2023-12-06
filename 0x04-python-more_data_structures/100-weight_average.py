#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    x = 0
    y = 0

    for z in my_list:
        x += z[0] * z[1]
        y += z[1]

    return (x/ y)
