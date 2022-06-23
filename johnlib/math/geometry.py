"""
General geometry-related math functions

usage:
area = circle_area(diameter)
area = rectangle_area(length, width)
"""
from math import pi

def circle_area(diameter):
    """
    Calculate area of a circle, given the diameter.

    :param diameter: Diameter of circle
    :return: area of circle
    """
    radius = diameter / 2
    area = pi * radius ** 2
    return area

def rectangle_area(length, width):
    """
    Calculate area of a rectangle.

    :param length: Length of one side
    :param width: Length of other side
    :return: area of rectangle
    """
    area = length * width
    return area

def spam(foo, bar, blah):
    """
    Function description....

    :param foo:
    :param bar:
    :param blah:
    :return:
    """
