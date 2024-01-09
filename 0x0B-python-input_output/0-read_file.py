#!/usr/bin/python3
"""this shows a text file to be handled."""


def read_file(filename=""):
    """displays the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
