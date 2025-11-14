#what is encapsulation?
'''ncapsulation means wrapping data (variable ) and methods into a single unit(class).
It helps to project data from being accessed or modified directly from outside the class.'''

#Access modifiers in python
'''1.public
2.protected
3.private'''

#Example 1:Public member
class Student:
     def __init__(self, name, age):
        self.name = name      # public
        self.age = age        # public
     def display(self):
         print(f"name:{self.name}, age:{self.age}")

s1=Student("sajeeb",221)
s1.display()

print(s1.name)
print(s1.age)

# eXAMPLE-2.protected members
class Student:
    def __init__(self, name, age):
        self._name = name      # protected
        self._age = age

    def display(self):
        print(f"Name: {self._name}, Age: {self._age}")

class CollegeStudent(Student):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def show_details(self):
        print(f"{self._name} is studying {self.course}")

# Test
s1 = CollegeStudent("Sajeeb", 21, "AI and Data Science")
s1.display()
s1.show_details()

#Eample-3.private members
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary    # private

    def show(self):
        print(f"Employee: {self.name}, Salary: {self.__salary}")

e1 = Employee("Sajeeb", 80000)
e1.show()

# Try accessing directly
print(e1.name)
# print(e1.__salary)   # ❌ This will cause an error

# example-4;Accessing private variables safely
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    # Getter method
    def get_salary(self):
        return self.__salary

    # Setter method
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary!")

e1 = Employee("Sajeeb", 80000)
print("Old Salary:", e1.get_salary())
e1.set_salary(90000)
print("Updated Salary:", e1.get_salary())

#Example-5.Name mangling in private variables
class Demo:
    def __init__(self):
        self.__hidden = "This is private"

obj = Demo()

# Access through name mangling
print(obj._Demo__hidden)


#-------Real lif example----
'''Imagine a Bank Account 
account number--->private
balance --->private
deposite/with draw--->controlled through public methods'''

class BankAccount:
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"{self.__name}'s balance is {self.__balance}")

# Test
acc = BankAccount("Sajeeb", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()


