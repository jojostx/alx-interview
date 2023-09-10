#!/usr/bin/python3
"""
defines a function island_perimeter
"""


def island_perimeter(grid):
    """
    Returns the Area of an island defines in grid
    """
    len_grid = len(grid)
    length1 = 0  # Used to count the length of the island
    length2 = 0  # Holds the length of the island
    width1 = 0  # Use to count the width of the island
    width2 = 0  # Holds the width of the island
    # counts the length of the grid
    for i in range(len_grid):
        if i > len(grid[i]) - 1:
            break
        for z in range(len_grid):
            if grid[z][i] == 1:
                length1 += 1
                if z != len_grid - 1 and grid[z + 1][i] == 0:
                    break
        if length1 > length2:
            length2 = length1
        length1 = 0
    # counts the width of the grid
    for i in range(len_grid):
        for z in range(len(grid[i])):
            if grid[i][z] == 1:
                width1 += 1
                if z != (len(grid[i]) - 1) and grid[i][z + 1] == 0:
                    break
        if width1 > width2:
            width2 = width1
        width1 = 0
    return ((length2 * 2) + (width2 * 2))
