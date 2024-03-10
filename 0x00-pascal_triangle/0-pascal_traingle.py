#!/usr/bin/python3
"""
a function that computes pascal triangle
"""


def pascal_triangle(n):
    """
    create pascal triangle with n number of rows
    """
    # create empty list to contain triangle
    triangle = []
    # return triangle if n is less than 0r equal 0
    if n <= 0:
        return triangle
    # a loop to generate n number of rows
    for i in range(n):
        # set the row to start with 1
        row = [1]
        # if there is a previous triangle
        if triangle:
            # get the previous row
            last_row = triangle[-1]
            # sum the adjacent number in previous row
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            # append 1 to the end of the row
            row.append(1)
        # append the row to the triangle
        triangle.append(row)
    return triangle

