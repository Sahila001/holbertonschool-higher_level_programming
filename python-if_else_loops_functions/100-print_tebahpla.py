#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{0}{1}".format(chr(122 - i), chr(90 - i) if i % 2 == 1 else ""), end="")
