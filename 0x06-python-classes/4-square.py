#!/usr/bin/python3
"""Square."""


class Square:
    """a square."""

    def __init__(self, size=0):
        """new square.
        Args:
            size (int): The len new square.
        """
        self.size = size

    @property
    def size(self):
        """sets size of  square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("an integer")
        elif value < 0:
            raise ValueError("size >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return (self.__size * self.__size)

