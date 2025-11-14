#what is inheritance?
'''Inheritance allows one class to use the properties and methods of anoter class'''
#example of real life
'''Parent class-->base/super class
   child class--->derived /sub class'''
#basic syntax
'''class Parent:
    #parent class code
class Child(parent):
    #child class inherits parents'''

#single inheritance
class Animal:
    def sound(self):
        print("Animal make sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks!")

d=Dog()
d.sound()#inherited from animal
d.bark() #Dog own method

#2.using super() with method
'''super() allows child class to call parent class tomorrow'''
class person:
   def __init__(self, name):
       self.name=name
class Student(person):
    def __init__(self, name,roll):
        super().__init__(name)  # calling parent constructor
        self.roll = roll

s1=Student("sajeeb",101)
print(s1.name,s1.roll)

# Multiple Inheritance
'''Grandparent-->Parent-->child'''
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(B):
    def showC(self):
        print("Class C")

obj = C()
obj.showA()
obj.showB()
obj.showC()

#Multiple inheritance
class Father:
    def skill(self):
        print("Father:Business skill")

class Mother:
    def talent(self):
        print("Mother:cooking skills")

class Child(Father,Mother):
    pass
c=Child()
c.skill()
c.talent()

#method overriding(polymorphism)
class Animal:
    def sound(self):
        print("Animal make sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks!")

d=Dog()
d.sound()

#Real life mini example :bank account
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

class SavingsAccount(BankAccount):
    def add_interest(self):
        self.balance += self.balance * 0.05

acc = SavingsAccount("Sajeeb", 1000)
acc.deposit(500)
acc.add_interest()
print("Final Balance:", acc.balance)
