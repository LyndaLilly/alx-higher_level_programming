#!/usr/bin/python3

def safe_print_division(a, b):
    """gives the product of a and b."""
    try:
        x = a / b
    except (TypeError, ZeroDivisionError):
        x = None
    finally:
        print("Inside result: {}".format(x))
    return (x)
