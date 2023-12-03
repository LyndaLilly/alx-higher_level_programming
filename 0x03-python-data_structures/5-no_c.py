#!/usr/bin/python3
def no_c(my_string):
    x = ""
    for p in my_string:
        if p != "c" and p != "C":
            x += p
    return x
