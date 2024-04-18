class Animal:
    def eat(self):
        print("Animal is eating...")

class Dog(Animal):
    def bark(self):
        print("Dog is barking...")

class Labrador(Dog):
    def wag_tail(self):
        print("Labrador is wagging tail...")

labrador = Labrador()
labrador.eat()  # Output: Animal is eating...
labrador.bark()  # Output: Dog is barking...
labrador.wag_tail()  # Output: Labrador is wagging tail...
