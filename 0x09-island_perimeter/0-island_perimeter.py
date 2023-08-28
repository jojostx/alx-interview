#!/usr/bin/python3
"""A function that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """This function will take a list of list of integers and use
       that to calculate how the perimeter of the island described in grid
    """
    perimeter = j = i = 0
    nc = len(grid)

    while i < nc:
        while j < nc:
            n = grid[i][j]
            if n == 1:
                above = i - 1
                left = j - 1
                right = j + 1
                below = i + 1

                if above < 0 or grid[above][j] != 1:
                    perimeter += 1

                if left < 0 or grid[i][left] != 1:
                    perimeter += 1

                if right > nc or grid[i][right] != 1:
                    perimeter += 1

                if below > nc or grid[below][j] != 1:
                    perimeter += 1
            j += 1

        i += 1
        j = 0

    return perimeter
