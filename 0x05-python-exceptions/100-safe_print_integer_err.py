#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    when there is error message prints to standard error.

    Args:
        value (int): this is the int to print.

    Returns:
       if there is error it will be false.
       rather - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
