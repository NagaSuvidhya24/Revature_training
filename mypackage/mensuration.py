""" Area, Circumference of SQ,Rectangle, Circle"""

from math import pi


def area_of_square(side):
    """
    :param side: Side of square
    :return:
    """
    return side * side

def area_of_circle(radius):
    """

    :param radius: Radius of Circle
    :return:
    """
    return pi * radius * radius

def area_of_recangle(len,brd):
    """
    :param len:Length of rectangle
    :param brd: Lreadth of rectangle
    :return:
    """
    return len * brd

def circumference(radius):
    """
    :param radius: Radius of Circle
    :return:
    """
    return 2 * pi * radius
