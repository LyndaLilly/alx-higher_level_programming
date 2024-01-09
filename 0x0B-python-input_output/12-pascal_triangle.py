#!/usr/bin/python3
"""Pascal's Triangle function."""


def pascal_triangle(n):
    """Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    rt = [[1]]
    while len(rt) != n:
        qe = rt[-1]
        x = [1]
        for y in range(len(qe) - 1):
            x.append(qe[y] + qe[y + 1])
        x.append(1)
        rt.append(x)
    return rt
