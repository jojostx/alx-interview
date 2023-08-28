#!/usr/bin/python3
"""A function that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """This function will take a list of list of integers and use
       that to calculate how the perimeter of the island described in grid
    """
    grid = [
        [0, 1, 0, 0, 0, 0],
        [3, 1, 4, 0, 0, 0],
        [5, 1, 6, 11, 0, 0],
        [7, 1, 1, 1, 12, 0],
        [0, 8, 9, 10, 0, 0]
    ]

    perimeter = 0
    j = i = 0
    nc = len(grid)

    while i < nc:
        while j < nc:
            n = grid[i][j]
            if n == 1:
                t = i - 1
                l = j - 1
                r = j + 1
                b = i + 1
                # top = 0 # [i-1][j]
                if t < 0 or grid[t][j] != 1:
                    print(grid[t][j])
                    perimeter += 1

                # left = 0 # [i][j-1]
                if l < 0 or grid[i][l] != 1:
                    print(grid[i][l])
                    perimeter += 1

                # right = 0 # [i][j+1]
                if r > nc or grid[i][r] != 1:
                    print(grid[i][r])
                    perimeter += 1

                # bottom = 0 # [i+1][j]
                if b > nc or grid[b][j] != 1:
                    print(grid[b][j])
                    perimeter += 1
            j += 1

        i += 1
        j = 0

    return perimeter

island_perimeter([])