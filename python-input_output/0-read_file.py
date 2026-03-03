#!/usr/bin/python3
"""
Module 0-read_file
Defines a function that reads a UTF-8 text file and prints it
to standard output.
"""


def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout"""
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
