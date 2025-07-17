class Circle:
    pi = 3.14159  # class attribute (shared across all instances)

    def __init__(self, radius):
        self.radius = radius  # instance attribute

    def area(self):
        return Circle.pi * self.radius ** 2

c = Circle(5)
print(c.area())      # Output: 78.53975
print(Circle.pi)     # Accessing class attribute



'''
Concept	Meaning
__init__	Constructor method, called when object is created
self	Reference to the current object
Attributes	Variables that belong to the object
Methods	Functions that belong to the object
Class Attributes	Shared across all instances
Inheritance	Allows one class to extend another
'''