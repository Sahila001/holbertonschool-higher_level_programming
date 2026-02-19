#!/usr/bin/python3
"""
Module for adding two integers.
Provides a function to add integers or floats.
Floats are casted to integers.
Raises TypeError if inputs are not numbers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Returns the sum of a and b.
    Raises TypeError if inputs are not numbers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
