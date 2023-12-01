#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lm = my_list[:]
    for x, y in enumerate(my_list):
        if y % 2 == 0:
            lm[x] = True
        else:
            lm[x] = False
    return(lm)
