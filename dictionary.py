# what is dictionary
'''A dictionary is an unordered, mutable collection of key-value pairs.
Each key maps to a value. Keys must be hashable (immutable types like strings,
numbers, tuples); values can be any type.'''

#dictionary syntax:
dictionary_name={
    "key1":"value1",
    "key2":"value2",
    "key3":"value3"
}
print(dictionary_name)

#another example
student = {
    "name": "Sajeeb",
    "age": 22,
    "department": "CSE",
    "cgpa": 3.85
}
print(student)

#accessing dictionary value
'''dictionary_name[key]
or
dictionary_name.get(key,default_values)
'''
student = {
    "name": "Sajeeb",
    "age": 22,
    "department": "CSE",
    "cgpa": 3.85
}

# Accessing value using key
print(student["name"])       # Output: Sajeeb

# Using .get() method (safe way)
print(student.get("age"))    # Output: 22

# If key not found, provide default
print(student.get("country", "Not Found"))  # Output: Not Found


#1.Additing new key-value pair
#syntax:
#dictionary_name[new_key]=Value
#example
student['university']='ius'
print(student)


#2.updating new exiting values
#dictionary_name[key] = new_value
#example:
student['cgpa']=3.90
print(student)

#3.removing items from dictionary
#using pop
student.pop('age')
print(student)
#using del
del student['department']
print(student)
#using clear()
student.clear()
print(student)
#using del entire
del student

#------example summery code------
student = {
    "name": "Sajeeb",
    "age": 22,
    "department": "CSE",
    "cgpa": 3.85
}

# Access
print(student["name"])
print(student.get("country", "Not Found"))

# Add new key
student["university"] = "IUS"

# Update existing key
student["cgpa"] = 3.90

# Remove one key
student.pop("age")

# Print final result
print(student)

#-----dictionary method-----

#1.keys() returns a view object that shows all the keys in the dictionary.
#syntax: dictionary_name.keys()
student = {
    "name": "Sajeeb",
    "age": 20,
    "department": "CSE"
}

print(student.keys()) #output dict_keys(['name', 'age', 'department'])

#2.values()-get all values
#syntax: dictionary_name.values()
#example:
print(student.values())#output:dict_values(['Sajeeb', 22, 'CSE'])
# you can loop through it like this:
for value in student.values():
    print(value)#output:dict_values(['Sajeeb', 22, 'CSE'])
    
#3.items()-get key-value pairs.It returns both keys and values as tuples inside a list-like object.
#syntax: dictionary_name.items()
#--example--
print(student.items())#output :dict_items([('name', 'Sajeeb'), ('age', 22), ('department', 'CSE')])
#by using loop
for key,value in student.items():
    print(f"{key}:{value}")
'''output:
name: Sajeeb
age: 22
department: CSE'''

#4.update()-Merge or Modify dictionary
#syntax: dictionary_name.update({key: value})
student.update({"cgpa": 3.9, "university": "IUS"})
print(student)#output:{'name': 'Sajeeb', 'age': 22, 'department': 'CSE', 'cgpa': 3.9, 'university': 'IUS'}

#dictionary comprehension in python
#dictionary comprehension is a compact and elegant way to create dictionary in a single line--just like list comprehensions but for key value pairs
#1.create dictionary from range
squares={x:x**2 for x in range(1,6)}
print(squares)#output:{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#convert list into dictionary
names = ["Sajeeb", "Rafi", "Nusrat"]
lengths = {name: len(name) for name in names}
print(lengths)

#filtering with condition
numbers=[1,2,3,4,5,6]
even_square={x: x**2 for x in numbers if x%2==0}
print(even_square)

#swap keys and values
fruits = {"apple": 1, "banana": 2, "mango": 3}
swapped = {v: k for k, v in fruits.items()}
print(swapped)
#ourput:{1: 'apple', 2: 'banana', 3: 'mango'}

#problem 1: create a dictionary to strore a students informartion
student={
    'name':'sajeeb',
    'age':'22',
    'uni':'ius',
    'dept':'cse'
}
print('name:', student['name'])
print('age:', student['age'])
print('uni:', student['uni'])
print('dept:', student['dept'])



#problem 2:Add a new key value pair to the existing dictionary


# Existing dictionary
student = {
    "name": "Sajeeb Khan",
    "age": 22,
    "department": "CSE",
    "GPA": 3.85
}

# Adding a new key-value pair
student["semester"] = 7

# Printing updated dictionary
print("Updated Dictionary:", student)















