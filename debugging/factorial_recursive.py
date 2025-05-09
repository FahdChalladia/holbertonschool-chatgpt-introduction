#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function to compute the factorial of a given number using recursion.

    Parameters:
        n (int): The number for which the factorial is calculated.

    Returns:
        int: The factorial of the number `n`. Returns 1 if `n` is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the number from command-line argument and calculate its factorial
f = factorial(int(sys.argv[1]))
print(f)
