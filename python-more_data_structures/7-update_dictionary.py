#!/usr/bin/python3
"""
Module that replaces or adds key/value in a dictionary
"""


def update_dictionary(a_dictionary, key, value):
    """
    Updates a dictionary with key/value:
    - Replaces the value if key exists
    - Adds the key/value if key does not exist
    Returns the updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
