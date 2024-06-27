#!/usr/bin/python3
import math
"""
class of Animal
"""
from abc import ABC, abstractmethod


class Shape():
    """
    """
    @abstractmethod
    def area(self):
        raise (TypeError(""))
    
    @abstractmethod
    def perimeter(self):
        raise (TypeError(""))

class Circle(Shape):
    """
    """
    def __init__(self, radius):
        if radius < 0:
            raise (AssertionError("Perimeter should handle negative radius"))
        self.radius = radius
    
    def area(self):
        return (math.pi * self.radius ** 2)
    
    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        if perimeter < 0:
            raise (AssertionError("Perimeter should handle negative radius"))
        else:
            return perimeter


class Rectangle(Shape):
    """
    """
    def __init__(self, width, height):
        if width < 0 and height < 0:
            raise (AssertionError("Perimeter should handle negative radius"))
        self.width = width
        self.height = height
    
    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        perimeter = 2*(self.width + self.height)
        return perimeter

def shape_info(shape):
    try:
        area = shape.area()
        perimeter = shape.perimeter()
        print (f"Area: {area}")
        print (f"Perimeter: {perimeter}")
    except AttributeError:
        print("El objeto no tiene métodos area o perimetro.")
