'''#opening file
#syntax: file=open(filename,mode)
#reading files
file=open("sample.txt","r")
data=file.read()
print(data)
file.close()

#example 2
file=open("sample.txt","r")
line1=file.readline()
line2=file.readline()
print(line1)
print(line2)
file.close()

#file writing mode='w','a','w+'
#syntax:
file = open("filename.txt", "w")  # open file in write mode
file.write("Your text here")      # write data into file
file.close()                      # close file after writing

#example 1--writing a sigle line 
file=open("hello.txt","w")
file.write("Hello, sajeeb khan this is your first line written by python")
file.close()
print("file written successfully!")
'''
#example2--writing multiple lines
file = open("data.txt", "w")
file.write("Line 1: Python is fun.\n")
file.write("Line 2: File handling is useful.\n")
file.write("Line 3: Let's learn step by step.")
file.close()

#example 3--writing list (using writelines())
lines = [
    "Python makes file handling easy.\n",
    "You can read and write files.\n",
    "Use write() or writelines().\n"
]

file = open("info.txt", "w")
file.writelines(lines)
file.close()
#example-4--using with statement
with open("note.txt","w") as f:
    f.write("this file is created using 'with'.\n")
    f.write("this file is   automatically closes thg file.\n")

#appending
file = open("filename.txt", "a")  # Open in append mode
file.write("Your new text\n")     # Add new data
file.close()    # Close the file

#example 1--appending text to a file
'''line 1:Python is fun.
line 2:File handling is useful.'''

file=open("data.txt","a")
file.write("\nline 3:appending new data")
file.close()
print("data is appended successfully")

#example appending multiple lines
file = open("data.txt", "a")
file.writelines([
    "\nLine 4: You can append lists too!",
    "\nLine 5: Python makes this easy."
])
file.close()
print("sajeeb its appended successfully")

#using with for appending
with open("log.txt","a") as f:
    f.write("user logged in at 10.00\n")
    f.write("user performed an action.\n")


#The with block automatically handles closing.

#Closing Files (close() and with Statement)
#syntax:
file=open("example.txt","w")
file.write("this is some text.")
file.close()
#problem without close()
file = open("data.txt", "w")
file.write("Hello, world!")
# No file.close() here!

#writing with 
with open("myfile.txt","w") as file:
    file.write("this is written using the with statement")
    print("file close automatically successfully")

#reading with
with open("myfile.txt","r") as file:
    content=file.read()
    print(content)
    print("file closed automatically after reading")

#appending with
with open("log.txt","a") as file:
    file.write("\nAppended using with statement.")
    print("appended with successfully")

#-----working with file path-----
#example 1--import the module
import os

#example 2--get current working directory

import os
print("current working directory:",os.getcwd())#output:os.getcwd() → returns the folder where your Python file is currently running

#example 3--check the file exists
import os
if os.path.exists("note.txt"):
    print("file exist")
else:
    print("file not found")

#example 4---create a folder
'''import os
os.mkdir("sajeeb khan ")
print("folder created successfully")'''

#example 5--list file in a dictionary
'''import os

print(os.listdir())'''

#example--6 jon paths safely
import os

path = os.path.join("C:\\Users\\Sajeeb", "Documents", "data.txt")
print(path)

'''# example 7---remove a  file folder
import os
#remove file
os.remove("old_file.txt")
#remove folder(only if empty)
os.rmdir("oldFoler")'''

#some practice now
#Write a Python program that writes your name and department into a file named info.txt.
with open("info.txt","w") as f:
    f.write("name:sajeeb khan\n")
    f.write("department:computer science\n")
    print("data written successfully")

#2.write a list of fruits to a file
fruits = ["apple", "banana", "cherry"]

with open("fruits.txt", "w") as f:
    for fruit in fruits:
        f.write(fruit + "\n")

print("✅ Fruits written successfully!")

#3.write multiple line using writelines()
lines=["python is powerful\n","file handling is useful\n","practice makes you perfect"]
with open("notes.txt","w") as f:
    f.writelines(lines)
print("multiple lines writen successfully")

'''#4.write user input to a file
"""ask the user for their favorite quote and save it into a file called quote.txt"""
quote=input("enter your favorite quote:")
with open("quote.txt","w") as f:
    f.write("your favorite quote:"+quote)
print("quote saved successfully")
'''
#5.combine writing and reading 
'''write a few sentences to a file and then read and display them'''
with open("message.txt","w") as f:
    f.write("Hello this is python file handling\n")
    f.write("you are learning how to write and read files.\n")
with open("message.txt","r") as f:
    content=f.read()
    print("file content:\n",content)

#6.write even number to a file
'''write all even numbers from 1 to 20 into a file called even_number.txt, each number on a new line'''
with open("even_numbers.txt","w") as f:
    for i in range (1,21):
        if i%2==0:
            f.write(str(i)+"\n")
print("even number is written successfully")

#7.write dictionary data into a file
'''write this dictionary into a file called student.txt'''
student={'name':'sajeeb','dept':'cse','cgpa':3.50}
with open('student.txt','w') as f:
    for key,value in student.items():
        f.write(f'{key}:{value}\n')
        print('student data saved successfully')
#8.write a multiplication table
'''ask the user for a number and write its multiplication table(1,10) in a file named table.txt'''
num=int(input('enter a number:'))
with open('table.txt','w') as f:
    for i in range (1,11):
        f.write(f'{num}*{i}={num*i}\n')
        print('multiplication table written successfully')

#9 sava user data for multiple people
'''Ask the user to enter names of 3 friends, and write all names in a file named friends.txt'''
with open("friends.txt", "w") as f:
    for i in range(3):
        name = input(f"Enter friend {i+1} name: ")
        f.write(name + "\n")

print("✅ All names saved successfully!")

#10.Store logs with timestamps
'''whenever the user runs the program, it should record'program started' with the current data and time in log.txt'''
import datetime
with open('log.txt','w') as f:
    time=datetime.datetime.now()
    f.write(f'program started at:{time}\n')
    print('log created successfully')