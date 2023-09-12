#!/usr/bin/python3
"""
Shebang to create a python script
"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row."""
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) < n:
        row = [1]
        for i in range(1, len(triangle[-1])):
            row.append(triangle[-1][i - 1] + triangle[-1][i])
        row.append(1)
        triangle.append(row)

    return triangle
