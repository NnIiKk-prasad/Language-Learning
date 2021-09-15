# -----Abstract Base Class & @abstractmethod-----
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 4

    def area(self):
        return self.length * self.breadth


# obj = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract method area
rect1 = Rectangle()
print(rect1.area())
