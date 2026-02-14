class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):   # Inheriting
    def bark(self):
        print("Dog is barking")


d = Dog()
d.eat()   # From parent
d.bark()  # From child
