#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): where the num will be printed.
        x (int): this is the number to print.

    Returns:
        this is the number printed.
    """
    pere = 0
    for q in range(x):
        try:
            print("{}".format(my_list[q]), end="")
            pere += 1
        except IndexError:
            break
    print("")
    return (pere)
