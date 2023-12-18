#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """this divides two elements.

    Args:
        my_list_1 (list): this is the 1st el.
        my_list_2 (list): this is is the 2nd el.
        list_length (int): this is the num of el to dividr.

    Returns:
       this sis the new lengthns.
    """
    yp = []
    for p in range(0, list_length):
        try:
            div = my_list_1[p] / my_list_2[p]
        except TypeError:
            print("wrong type")
           q = 0
        except ZeroDivisionError:
            print("division by 0")
            q = 0
        except IndexError:
            print("out of range")
            q = 0
        finally:
            yp.append(q)
    return (yp)
