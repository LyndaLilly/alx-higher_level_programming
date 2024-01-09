#!/usr/bin/python3
"""text file insertion func"""


def append_after(filename="", search_string="", new_string=""):
    """contain a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    st = ""
    with open(filename) as r:
        for pr in r:
            st += pr
            if search_string in pr:
                st += new_string
    with open(filename, "w") as w:
        w.write(st)
