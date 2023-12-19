#!/usr/bin/python3
"""class Square."""


class Square:
    """shows a square."""

    def __init__(self, size=0):
        """a new square.
        Args:
            size (int): The len of square.
        """
        if not isinstance(size, int):
            raise TypeError("an integer")
        elif size < 0:
            raise ValueError("size >= 0")
        self.__size = size

    def area(self):
        """Return area of square."""
        return (self.__size * self.__size)
