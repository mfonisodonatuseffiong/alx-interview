#!/usr/bin/python3
"""
0-pascal_triangle
This module provides a function to generate Pascal's Triangle.
"""

def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.

    Args:
        n (int): Number of rows in Pascal's Triangle.

    Returns:
        List[List[int]]: A list of lists representing Pascal's Triangle,
                         or an empty list if n <= 0.
    """
    triangle = []
    
    if n <= 0:
        return triangle
    
    triangle.append([1])  # Start with the first row.

    for i in range(1, n):
        row = [1]  # Start each row with a '1'.
        last_row = triangle[i - 1]
        
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j + 1])  # Compute the inner elements.
        
        row.append(1)  # End each row with a '1'.
        triangle.append(row)  # Add the completed row to the triangle.

    return triangle  # Return the complete Pascal's Triangle.
