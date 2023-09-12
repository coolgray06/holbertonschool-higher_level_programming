#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix_row = []
        for element in row:
            new_matrix_row.append(element**2)
        new_matrix.append(new_matrix_row)
    return(new_matrix)
