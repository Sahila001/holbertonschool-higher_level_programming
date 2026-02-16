#!/usr/bin/python3
"""
Module that returns a new dictionary with all values multiplied by 2
"""


def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2
    Original dictionary is not modified
    """
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dict
