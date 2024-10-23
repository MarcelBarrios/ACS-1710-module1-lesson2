#WHY =  make it easy to pass the results of a function to another function

from typing import Any


class Car:
    wheels = 4

    def __init__(self, arg1):
        self.color = arg1

    def __call__(self, func):
        self.color = func()

    def paintCar(self, arg1):
        self.color = arg1

    def details(self):
        print("color = ", self.color)

# init a car
car1 = Car("red")
car1.paintCar("blue")

@car1
def changeColorWithSemantic():
    return "yellow"

car1.details()