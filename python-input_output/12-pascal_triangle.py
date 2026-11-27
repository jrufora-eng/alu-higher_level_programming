#!/usr/bin/python3
"""Module that defines pascal_triangle."""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]
    for _ in range(1, n):
        prev_row = triangle[-1]
        row = [1]
        for idx in range(1, len(prev_row)):
            row.append(prev_row[idx - 1] + prev_row[idx])
        row.append(1)
        triangle.append(row)

    return triangle
