#!/usr/bin/python3
""" This module defines a class Square """


class Square:
    """ This class defines a square by its size and returns its area"""

    def __init__(self, size=0):
        """ Initialize the size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ This function returns the area of the square. """
        return self.__size ** 2
