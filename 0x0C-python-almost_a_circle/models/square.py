#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """displays a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """sets a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): x coordinate of the new Square.
            y (int): y coordinate of the new Square.
            id (int): id of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """sets size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
                - 1st arg displays id attribute
                - 2nd arg displays size attribute
                - 3rd arg displays x attribute
                - 4th arg displays y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            rt = 0
            for arg in args:
                if rt == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif rt == 1:
                    self.size = arg
                elif rt == 2:
                    self.x = arg
                elif rt == 3:
                    self.y = arg
                rt += 1

        elif kwargs and len(kwargs) != 0:
            for q, fi in kwargs.items():
                if q == "id":
                    if fi is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = fi
                elif q == "size":
                    self.size = fi
                elif q == "x":
                    self.x = fi
                elif q == "y":
                    self.y = fi

    def to_dictionary(self):
        """displays the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
