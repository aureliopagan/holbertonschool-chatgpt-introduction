#!/usr/bin/python3
import sys

def factorial(n):
    """
    Recursively calculates the factorial of a non-negative integer.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Parse input from command line, calculate factorial, and print result
f = factorial(int(sys.argv[1]))
print(f)
