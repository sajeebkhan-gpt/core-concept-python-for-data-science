#----practice session---
'''Create a custom module named calculator.py containing add,subtract,multiply and divide functions. 
Then import it into another file and test all functions'''
#2.
'''use random module to generate 
task 1:-- 10 random numbers between 1-100
task 2:-- A random name from a list of friends'''

#task 1 random number from multiple
import random

for i in range(10):
    random_number = random.randint(1, 100)
    print("The random number would be:", random_number)

#random number from single
import random
random_number=random.randint(1,100)
print ("the random number is :",random_number)

#task 2
import random
name=['sajeeb','tisha','akhi','monira']
random_select=random.choice(name)
print(random_select)

#or
random.shuffle(name)
print("shuffled  names:",name)

#datatime task
'''use datetime module to:
task-1-->print current date
task-2-->print only year and month
task-3-->add 7 days to today's date'''

 #task 1
import datetime
current=datetime.datetime.now()
print ("current date & time:",current)
#task 2:only year and month
print("year:",current.year, " month:", current.month)

#task3--add 7 days today's date
seven_days=current+datetime.timedelta(days=7)
print("after 7 days:",seven_days)
today = datetime.date.today()
print("Today's date:", today)
print("Today + 7 days:", today + datetime.timedelta(days=7))


#4.os module: create ,rename, delete a folder
import os
import shutil   # used to remove non-empty directories safely

folder_name = "test_folder"
renamed_folder = "renamed_folder"

# 1) Create folder if not exists
try:
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"Folder '{folder_name}' already exists.")
except OSError as e:
    print("Failed to create folder:", e)

# 2) Rename folder (only if original exists and new name not used)
try:
    if os.path.exists(folder_name) and not os.path.exists(renamed_folder):
        os.rename(folder_name, renamed_folder)
        print(f"Folder renamed to '{renamed_folder}'.")
    else:
        print("Rename skipped: source missing or destination already exists.")
except OSError as e:
    print("Failed to rename folder:", e)

# 3) Delete folder (be careful!)
try:
    if os.path.exists(renamed_folder):
        # If folder may contain files use shutil.rmtree, otherwise os.rmdir for empty
        # Here we'll use rmtree to be safe:
        shutil.rmtree(renamed_folder)
        print(f"Folder '{renamed_folder}' deleted.")
    else:
        print(f"Folder '{renamed_folder}' does not exist.")
except OSError as e:
    print("Failed to delete folder:", e)
