#!/usr/bin/python3
"""this the MyLis module"""


class MyList(list):
    """MyList class - gotten from list"""
    def print_sorted(self):
        """shows sorted list"""
        print(sorted(self))
