#!/usr/bin/python3
'''Island Perimeter
Calculates the perimeter of an island represented by a 2D grid.
'''


def island_perimeter(grid):

    ''' Get number of rows and columns in the grid '''
    row_len, col_len = len(grid), len(grid[0])
    p, con = 0, 0

    ''' Checks if grid is empty '''
    if not grid:
        return 0

    ''' Iterate through each cell in the grid '''
    for a in range(0, row_len):
        for b in range(col_len):

            ''' Check if the current cell represents land '''
            if grid[a][b] == 1:
                p += 4

                ''' Check for land to the left of cell '''
                if a != 0 and grid[a - 1][b] == 1:
                    con += 1
                ''' Check for land above cell '''
                if b != 0 and grid[a][b - 1] == 1:
                    con += 1

    ''' Returns the perimeter '''
    return p - (con * 2)
