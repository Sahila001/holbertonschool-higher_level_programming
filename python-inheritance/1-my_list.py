#!/usr/bin/python3
"""Module that defines a MyList class that inherits from list."""


class MyList(list):
    """Custom list class that prints a sorted version of itself."""

    def print_sorted(self):
        """Print a new sorted list (ascending order)."""
        sorted_list = sorted(self)
        print(sorted_list)
