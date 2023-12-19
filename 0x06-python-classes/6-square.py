#!/usr/bin/python3
"""class Square."""


class Square:
    """a square."""

    def __init__(self, size=0, position=(0, 0)):
        """new square.
        Args:
            size (int): len of new square.
            position (int, int): position of new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """sets size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("an integer")
        elif value < 0:
            raise ValueError("size >= 0")
        self.__size = value

    @property
    def position(self):
        """sets the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("a tuple of 2 integers")
        self.__position = value

    def area(self):
        """area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
