#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = []
    for line in matrix:
        x.append([c**2 for c in line])
    return x
