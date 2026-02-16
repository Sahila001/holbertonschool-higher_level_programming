#!/usr/bin/python3
"""
Module that deletes a key in a dictionary
"""


def simple_delete(a_dictionary, key=""):
    """
    Deletes key in a dictionary if it exists
    Returns the modified dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
