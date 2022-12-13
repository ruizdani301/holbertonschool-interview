#!/usr/bin/python3
"""Create a function def pascal_triangle(n): that returns a
   list of lists of integers representing the Pascal’s triangle of
"""


def pascal_triangle(n):
    """
    list of lists of integers representing the Pascal triangle of n
    """
    if n <= 0:
        return []

    pascal = []
    for x in range(n):
        base = [1]
        for z in range(x):
            base.append(sum(pascal[-1][z:z+2]))
        pascal.append(base)
    return pascal
