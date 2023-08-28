#!/usr/bin/python3
"""A function that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """This function will take a list of list of integers and use
       that to calculate how the perimeter of the island described in grid
    """
    perimeter = 0

    nc = len(grid)
    for i in range(nc):
      nr = len(grid[i])
      for j in range(nr):
          if grid[i][j] == 1:
              above = i - 1
              left = j - 1
              right = j + 1
              below = i + 1

              if above < 0 or grid[above][j] != 1:
                  perimeter += 1

              if left < 0 or grid[i][left] != 1:
                  perimeter += 1

              if right > nr or grid[i][right] != 1:
                  perimeter += 1

              if below > nc or grid[below][j] != 1:
                  perimeter += 1

    return perimeter
