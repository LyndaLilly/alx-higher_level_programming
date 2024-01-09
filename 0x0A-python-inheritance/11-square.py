#!/usr/bin/python3
"""defines square module"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """displays square class"""
    def __init__(self, size):
        """seting a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area of a square"""
        return self.__size ** 2

    def __str__(self):
        """returns a string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
