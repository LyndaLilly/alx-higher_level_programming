#!/usr/bin/python3
"""class Square."""


class Square:
    """a square."""

    def __init__(self, size):
        """new square.
        Args:
            size (int): The len  new square.
        """
        self.size = size

    @property
    def size(self):
        """sets size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("integer")
        elif value < 0:
            raise ValueError("size >= 0")
        self.__size = value

    def area(self):
        """Return area of square."""
        return (self.__size * self.__size)

    def my_print(self):
        """square with the # char."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")

