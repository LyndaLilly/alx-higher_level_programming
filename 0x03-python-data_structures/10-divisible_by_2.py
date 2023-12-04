#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nl = []
    if my_list:
        for c in my_list:
            nl.append(False if c % 2 else True)
        return nl
