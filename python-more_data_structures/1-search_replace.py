#!/usr/bin/python3
"""
Module that replaces all occurrences of an element
in a list by another element
"""


def search_replace(my_list, search, replace):
    """
    Returns a new list with all occurrences of search replaced by replace
    The original list is not modified
    """
    return [replace if element == search else element for element in my_list]
