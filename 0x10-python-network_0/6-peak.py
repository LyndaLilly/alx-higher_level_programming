#!/usr/bin/python3
"""this gets a peak in unstored datas"""


def find_peak(list_of_integers):
    """this gets a peak in unstored datas"""

    if list_of_integers is None or list_of_integers == []:
        return None
    xy = 0
    ret = len(list_of_integers)
    abx = ((ret - xy) // 2) + xy
    abx = int(abx)
    if ret == 1:
        return list_of_integers[0]
    if ret == 2:
        return max(list_of_integers)
    if list_of_integers[abx] >= list_of_integers[abx - 1] and\
            list_of_integers[abx] >= list_of_integers[abx + 1]:
        return list_of_integers[abx]
    if abx > 0 and list_of_integers[abx] < list_of_integers[abx + 1]:
        return find_peak(list_of_integers[abx:])
    if abx > 0 and list_of_integers[abx] < list_of_integers[abx - 1]:
        return find_peak(list_of_integers[:abx])
