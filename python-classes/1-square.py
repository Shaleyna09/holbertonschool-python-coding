#!/usr/bin/python3
""" This module defines a class Square."""


class Square:

    """ This class defines a square by its size."""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
