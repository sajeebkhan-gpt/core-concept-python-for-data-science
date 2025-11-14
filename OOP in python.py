#|what is oop> oop is a programing style that helps you structure your code into ibjects--small, reusable, until that both data and fuctions
#syntax of a simple class in python
#---class example---#
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} car is starting...")

# Practice / usage
my_car = Car("toyota", "red")
print(my_car.brand)   # Expected output: toyota
print(my_car.color)   # Expected output: red
my_car.start()        # Expected output: toyota car is starting...

#class syntax
'''class ClassName:
    # class attributes (optional)
    # constructor (optional)
    # methods
'''
#example 1: A simple class and object
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

# Create objects
s1 = Student("Sajeeb", 101)
s2 = Student("Rahim", 102)

# Access data
s1.display()
s2.display()

#Example 2:Accessing and Modifying Attributes
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student("Sajeeb", 101)

# Access attributes
print(s1.name)
print(s1.roll)

# Modify attribute
s1.name = "Nafis"
print(s1.name)

#using multiple method in a class
class Calculator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mul(self, a, b):
        return a * b
    
    def div(self, a, b):
        return a / b

# Create object
calc = Calculator()

print("Addition:", calc.add(5, 3))
print("Subtraction:", calc.sub(5, 3))
print("Multiplication:", calc.mul(5, 3))
print("Division:", calc.div(5, 3))

#instance and class variable

class Student:
    def __init__(self, name, roll):
            self.name = name #instance variable
            self.roll = roll

  #create object
s1=Student("sajeeb",101)
s2=Student("tisha",102)

print(s1.name, s1.roll)
print(s2.name, s2.roll)

#2.class  variable
class Student:
    school = "IUS University"   # class variable (shared)

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student("Sajeeb", 101)
s2 = Student("Rahim", 102)

print(s1.name, "-", s1.school)
print(s2.name, "-", s2.school)

#changing the class variable
class Student:
    school = "IUS University"

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

s1 = Student("Sajeeb", 101)
s2 = Student("Rahim", 102)

Student.school = "Update University"   # changed using class name

print(s1.school)
print(s2.school)

#exaples with three method type
class Student:
    school = "IUS University"

    def __init__(self, name):
        self.name = name

    def show_info(self):   # instance method
        print(f"Name: {self.name}")

    @classmethod
    def change_school(cls, new_name):   # class method
        cls.school = new_name

    @staticmethod
    def greet():   # static method
        print("Welcome to the Student Management System!")

# Use them
Student.greet()                     # static method
s1 = Student("Sajeeb")
s1.show_info()                      # instance method
Student.change_school("Update IUS") # class method
print(Student.school)
