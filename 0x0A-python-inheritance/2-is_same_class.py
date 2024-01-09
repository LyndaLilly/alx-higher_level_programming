#!/usr/bin/python3
# 2-is_same_class.py
# Brennan D Baraban <375@holbertonschool.com>
"""givs the meaning of class-checking func"""


def is_same_class(obj, a_class):
    """this checks weda obj is an instance of a given class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
