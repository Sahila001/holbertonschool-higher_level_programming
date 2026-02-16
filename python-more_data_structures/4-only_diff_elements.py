#!/usr/bin/python3
"""
Module that returns a set of all elements present in only one set
"""


def only_diff_elements(set_1, set_2):
    """
    Returns a set with elements present in set_1 or set_2 but not both
    """
    return set_1 ^ set_2
