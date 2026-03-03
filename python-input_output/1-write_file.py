#!/usr/bin/python3
"""
Module 1-write_file
Defines a function that writes a string to a UTF-8 text file
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file and return number of characters"""
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
