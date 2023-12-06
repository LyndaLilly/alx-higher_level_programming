#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    x = a_dictionary.copy()
    for y, z in x.items():
        if value == z:
            a_dictionary.pop(y)
    return a_dictionary
