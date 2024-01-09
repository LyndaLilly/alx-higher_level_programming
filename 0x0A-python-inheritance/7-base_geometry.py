#!/usr/bin/python3
"""meanin of geometry class BaseGeometry."""


class BaseGeometry:
    """shows base geometry."""

    def area(self):
        """tis is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """clears parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
