#!/usr/bin/python3
"""shows a square."""


class Square:
    """a square."""

    def __init__(self, size=0):
        """brings a new Square.
        Args:
            size (int): length of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("an int")
        elif size < 0:
            raise ValueError("size >= 0")
        self.__size = size
