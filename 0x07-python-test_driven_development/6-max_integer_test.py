#!/usr/bin/python3
"""this gets the maximum int in a list
"""


def max_integer(list=[]):
    """this is a fun to set max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    opt = list[0]
    r = 1
    while r < len(list):
        if list[r] > opt:
            opt = list[r]
        r += 1
    return opt
