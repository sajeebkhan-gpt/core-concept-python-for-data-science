#what is module ?
#A module is a python file that contains functions,variable, and classes--which you can import and use in another python program
#example: math.py , random.py , datetime.py-- all are built in modules in python

#syntax: import module_name
# or--from module_name import function_name
#or--from module_name import*

#example--1 :using math module
import math

print(math.sqrt(25))      # Square root
print(math.pow(2, 3))     # 2 to the power of 3
print(math.pi)            # Constant pi

#example--2:importing specific functions
from math import sqrt, pi
print(sqrt(16))
print(pi)
#Now, you don’t need to write math.sqrt().

#2.creating your own module

#3.renaming modeules with as
import math as m
print(m.sqrt(9))
print(m.pi)
print(m.factorial(5))

#4.Importing everything from a module
from math import*
print(sqrt(49))
print(factorial(5))
print(pi)

#example of a common modules
#1.math module
import math
print("Square root:", math.sqrt(36))
print("Factorial:", math.factorial(5))
print("Pi value:", math.pi)

#2.random module
import random
print(random.randint(1,10))
print(random.choice(['apple','sjeeb','tisha']))

#3.datetime module
import datetime           
current_time=datetime.datetime.now()
print("current data and time:",current_time)

'''#4.os module
import os
print("current directory;",os.getcwd())
os.mkdir("test_folder")
'''
#---what is package---?
# A package is a collection of modules organized in directories
#---importing from package--
'''from mypackage.module1 import func1
or 
import mypackage .module1 as m1
m1.func1()'''

#Using dir() and help() functions
import math
print(dir(math))
help(math)