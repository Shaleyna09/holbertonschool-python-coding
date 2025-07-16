#!/usr/bin/python3
""" This module defines a calss Square """


class Square:
    """ This class defines a square by its size """

    def __init__(self, size=0):
        """ Initialize a square with a size """
        self.__size = size

    @property
    def size(self):
        """ Get the size of the square. """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size with validation. """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """ Returns the area of the given square. """
        return self.__size ** 2
