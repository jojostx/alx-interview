#!/usr/bin/python3
"""Rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    """a function that takes an n x n 2D matrix,
       rotates (in-place) it 90 degrees clockwise.
       args:
          matrix
    """
    r = 0
    c = 0
    n = len(matrix)
    temp = []

    while (r < n):
        while (c <= n):
            if c != n:
                temp.append(matrix[c][r])
            else:
                temp.reverse()
                matrix.append(temp.copy())
                temp = []
            c += 1
        c = 0
        r += 1

    c = 0
    while c < n:
        del matrix[0]
        c += 1
