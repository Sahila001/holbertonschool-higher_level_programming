#!/usr/bin/python3
"""
Module that adds all unique integers in a list
"""


def uniq_add(my_list=[]):
    """
    Returns the sum of all unique integers in the list
    """
    unique_numbers = []

    for number in my_list:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return sum(unique_numbers)
