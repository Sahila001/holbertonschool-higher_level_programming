#!/usr/bin/python3
"""
Module for adding two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        if a == float("inf") or a == float("-inf") or a != a:
            raise TypeError("a must be an integer")

    if isinstance(b, float):
        if b == float("inf") or b == float("-inf") or b != b:
            raise TypeError("b must be an integer")

    return int(a) + int(b)
