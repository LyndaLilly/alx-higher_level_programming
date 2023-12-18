#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """this prints the first num of x.

    Args:
        my_list (list): the list to print from.
        x (int): this is the num to be printrd.

    Returns:
        this is num of element printrf.
    """
    pere = 0
    for q in range(0, x):
        try:
            print("{:d}".format(my_list[q]), end="")
            pere += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (pere)
