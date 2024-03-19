#!/usr/bin/python3

"""
    Determine the minimun operations to return n H in a file.
"""

def minOperations(n):
    """
        A function to calculate the minimum number of operations 
        needed to give n H number of characters 
        args: n: The number of H characters to be returned
    """

    num_h = 1
    incrementor = 0
    counter = 0

    while num_h < n:
        remainder_h = n - num_h
        if (remainder_h % num_h == 0):
            incrementor = num_h
            num_h += incrementor
            counter += 2
        else:
            num_h += incrementor
            counter += 1
    return counter
