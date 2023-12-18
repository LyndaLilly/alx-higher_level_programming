#!/usr/bin/python3

def safe_print_integer(value):
    """prints int with "{:d}".format().

    Args:
        value (int): this is int to print.

    Returns:
       if error occurs - False.
       if not - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
