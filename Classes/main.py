class Dog:
    def __init__(self, name, breed):
        self.name = name      # attribute
        self.breed = breed    # attribute

    def bark(self):           # method
        print(f"{self.name} says Woof!")
''''
__init__ is the constructor – it runs when you create a new object from the class.

self refers to the current object.

name and breed are attributes.

bark is a method that prints a message.
'''

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()  # Output: Buddy says Woof!
