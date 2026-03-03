#!/usr/bin/python3
"""
Module 5-save_to_json_file
Defines a function that writes an object to a text file
using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file using JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
