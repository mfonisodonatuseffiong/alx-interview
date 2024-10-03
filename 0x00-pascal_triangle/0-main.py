#!/usr/bin/python3
"""
Main script to test the Pascal's Triangle function.
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(pascal_triangle):
    """
    Print the Pascal's Triangle.

    Args:
        pascal_triangle (List[List[int]]): The triangle to print.
    """
    for row in pascal_triangle:
        print(f"[{','.join(map(str, row))}]")  # Using f-strings for clarity.

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
