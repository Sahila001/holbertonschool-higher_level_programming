#!/usr/bin/python3
"""
Module that prints a dictionary sorted by keys
"""


def print_sorted_dictionary(a_dictionary):
    """
    Prints the dictionary by ordered keys (alphabetically)
    Only sorts the first-level keys
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
