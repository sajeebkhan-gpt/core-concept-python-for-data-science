#what is polymorphism?
'''In python polymorphism allows the same function or method name to behave differently depending on the object or data type'''
#Real world Example
'''Think about the word'read'
   *A teacher reads the book
   *A student reads the notebook
   *A child reads the cartoons

same action read, but action differs depending on who is performing it---> this is called polymorphism
'''

#1.Polymorphism with built in functions
print(len("hello"))
print(len([2,4,5]))
#same function len() works for string and list--->polymorphism

#polymorphism with classe
class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")
   #using polymorphism
for pet in (Dog(),Cat(),Animal()):
    pet.sound()

#Polymorphism with functions
class Bike:
    def move(self):
        print("Bike is moving")

class Car:
    def move(self):
        print("Car is moving")

def start(vehicle):
    vehicle.move()

start(Bike())
start(Car())

#4.Ploymorphism with method overloading 
class Math:
    def add(self, a, b, c=0):
        return a + b + c

obj = Math()
print(obj.add(2, 3))       # 5
print(obj.add(2, 3, 4))    # 9

#practice question
'''Q1. Create a Shape parent class and derived classes Circle and Square. Each class should have a method area(). 
Use polymorphism to call area for both.'''
class Shape:
    def area(self):
        print("Area is not defined for generic shape")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Polymorphism in action
shapes = [Circle(5), Square(4), Shape()]

for s in shapes:
    print(s.area())

'''Q2. Create a function make_sound(animal) 
that calls the sound method of Dog, Cat, and Cow classes.'''

class Dog:
    def sound(self):
        print("dog barks:woof woof")
class Cat:
    def sound(self):
        print("cat sound: meow")
class Cow:
    def sound(self):
        print("cow sound:Hamba")

def make_sound(animal):
    animal.sound()#same founction work for all animal

#calling the function with different object
make_sound(Dog())
make_sound(Cat())
make_sound(Cow())
