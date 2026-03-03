#!/usr/bin/python3
"""
Module 2-append_write
Defines a function that appends a string to a UTF-8 text file
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Append text to a UTF-8 file and return number of characters"""
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
