#!/usr/bin/python3
"""
Module that returns the key with the biggest integer value
"""


def best_score(a_dictionary):
    """
    Returns the key with the highest value
    If dictionary is None or empty, returns None
    """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    best_key = None
    best_value = None

    for key, value in a_dictionary.items():
        if best_value is None or value > best_value:
            best_value = value
            best_key = key

    return best_key
