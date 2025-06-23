#!/usr/bin/python3
""" This module defines a class Square"""


class Square:
    """ This class defines a square by its size"""
    def __init__(self, size=0):
        """ Initializes a square with a size."""
        self.__size = size

    @property
    def size(self):
        """ Gets the size of the square. """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets a value for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Returns the size of the given square. """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
