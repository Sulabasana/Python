class Animal:
    def speak(self):
        print("Animal makes a sound")

class Cat(Animal):
    def speak(self):  # Override method
        print("Meow")

class Dog(Animal):
    def speak(self):  # Override method
        print("Woof")

cat = Cat()
dog = Dog()
cat.speak()  # Output: Meow
dog.speak()  # Output: Woof
