#!/usr/bin/python3
"""meaning of rec subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """shows a square."""

    def __init__(self, size):
        """sets new square.
        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
