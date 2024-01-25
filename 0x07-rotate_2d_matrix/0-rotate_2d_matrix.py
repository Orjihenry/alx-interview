#!/usr/bin/python3
'''
Rotate 2D Matrix
first transpose, then reverse.
'''


def rotate_2d_matrix(matrix):
    ''' checks if matrix is a type of list '''
    if type(matrix) != list:
        return

    ''' checks if matrix is empty '''
    if len(matrix) < 1:
        return

    ''' first step, transpose the matrix '''
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    ''' reverse matrix '''
    n = len(matrix)
    for i in range(n//2):
        for j in range(n):
            matrix[j][i], matrix[j][n-1-i] = matrix[j][n-1-i], matrix[j][i]
