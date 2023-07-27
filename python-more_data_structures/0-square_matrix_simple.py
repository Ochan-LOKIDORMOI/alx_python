#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create an empty matrix to store the squared values
    new_matrix = []

    for row in matrix:
        new_row = []
        for element in row:
            squared_value = element ** 2
            new_row.append(squared_value)
        # Append the new_row list to the new_matrix list
        new_matrix.append(new_row)

    return new_matrix