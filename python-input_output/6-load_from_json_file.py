#!/usr/bin/python3
"""
Module 6-load_from_json_file
Defines a function that creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """Return a Python object from a JSON file"""
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
