#tuple in python
'''A tuple is an ordered collection of items 
which can be of different data types, numbers, strings , booleans ,
or even other tuples. Tuples are immutable, meaning that once they are created, 
their elements cannot be changed, added, or removed.'''
#differnece between list and tuple
#list is mutable but tuple is immutable
#Creating a tuple
my_tuple = (1, 2, 3, 'hello', True)
print(my_tuple)

t1=(1, 2, 3)
t2=4,5,6
t3=() #empty tuple
t4=(1,) #single element tuple
not_a_tuple=(1) #this is not a tuple
print(type(t4))
print(type(not_a_tuple))
print(t2)
#why the comma is necessary in single element tuple
single_element_tuple = (5,)
print(type(single_element_tuple))  # Output: <class 'tuple'>
not_a_tuple = (5)
print(type(not_a_tuple))  # Output: <class 'int'>

#example explanation line by line
example_tuple = (10, 20, 30, 'Python', False)
print(example_tuple)  # Output: (10, 20, 30, 'Python', False)
print(example_tuple[0])  # Output: 10
print(example_tuple[3])  # Output: Python
print(example_tuple[-1])  # Output: False
print(example_tuple[1:4])  # Output: (20, 30, 'Python')

#example of immutability
immutable_tuple = (1, 2, 3)
# immutable_tuple[0] = 10  # This will raise a TypeError
print(immutable_tuple)

#workaround to change tuple content:convert to list and back to tuple
temp_list = list(immutable_tuple)
temp_list[0] = 10
modified_tuple = tuple(temp_list)
print(modified_tuple)  # Output: (10, 2, 3)

#another example of workaround
t=(1, 2, 3, 4, 5)
lst=list(t) #output: [1, 2, 3, 4, 5]
lst[0]=99
t=tuple(lst)
print(t)  # Output: (99, 2, 3, 4, 5)

#indexing and slicing
sample_tuple = ('a', 'b', 'c', 'd', 'e', 'f')
print(sample_tuple[2])    # Output: 'c'
print(sample_tuple[-1])   # Output: 'f' starts from end
print(sample_tuple[1:4])  # Output: ('b', 'c', 'd') starts from index 1 to index 3
print(sample_tuple[:3])   # Output: ('a', 'b', 'c') starts from beginning to index 2
print(sample_tuple[3:])   # Output: ('d', 'e', 'f ) starts from index 3 to end
print(sample_tuple[:])    # Output: ('a', 'b', 'c', 'd', 'e', 'f') entire tuple

# concatenation and repetition
tuple1=(1,2,3)
tuple2=(4,5,6)
concatenated_tuple=tuple1+tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)
repeated_tuple=tuple1*3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

#membership testing
test_tuple=('x', 'y', 'z')
print('y' in test_tuple) # Output: True
print('a' not in test_tuple) # Output: True
print('a' in test_tuple) # Output: False

#iteration and looping
iter_tuple = (10, 20, 30)
for item in iter_tuple:
    print(item)
# Output:
# 10
# 20
# 30
# tuple packing and unpacking
packed_tuple = 1, 'hello', 3.14
print(packed_tuple)  # Output: (1, 'hello', 3.14
a, b, c = packed_tuple
print(a)  # Output: 1
print(b)  # Output: hello
print(c)  # Output: 3.14

#swapping values using tuple unpacking
x = 5
y = 10
x, y = y, x
print(x)  # Output: 10
print(y)  # Output: 5   

#built-in functions with tuples
num_tuple=(3, 1, 4, 1, 5, 9)
print(len(num_tuple))  # Output: 6
print(min(num_tuple))  # Output: 1
print(max(num_tuple))  # Output: 9
print(sum(num_tuple))  # Output: 23
print(sorted(num_tuple))  # Output: [1, 1, 3, 4, 5, 9]
print(tuple(reversed(num_tuple)))  # Output: (9, 5, 1, 4, 1, 3)
print(num_tuple.count(1))  # Output: 2
print(num_tuple.index(4))  # Output: 2

#nested tuples
nested_tuple=(1, 2, (3, 4), (5, 6, (7, 8)))
print(nested_tuple)  # Output: (1, 2, (3, 4), (5, 6, (7, 8)))
print(nested_tuple[2])  # Output: (3, 4)
print(nested_tuple[3][2])  # Output: (7, 8)
print(nested_tuple[3][2][1])  # Output: 8

#tuple methods
#tuples have only two built-in methods: count() and index()
sample_tuple = (1, 2, 2, 3, 4, 2)
print(sample_tuple.count(2))  # Output: 3(2 appears 3 times)
print(sample_tuple.index(3))  # Output: 3(position of first occurrence of 3)

#use cases of tuples
#1.Data integrity
coordinates = (40.7128, -74.0060)  # Latitude and Longitude of New York City
print(coordinates)
#2.Dictionary keys
location_data = {
    (40.7128, -74.0060): "New York City",
    (34.0522, -118.2437): "Los Angeles",
    (41.8781, -87.6298): "Chicago"
}
print(location_data)

#3.Returning multiple values from functions
def get_min_max(numbers):
    return(min(numbers),max(numbers))
result=get_min_max([3, 1, 4, 1, 5, 9 ])
print(result)  # Output: (1, 9)

#4.Unpacking multiple values
point = (10, 20)
x,y=point
print(x)  # Output: 10
print(y)  # Output: 20

#5.Immutability requirement
def calculate_area(dimensions):
    length, width = dimensions
    return length * width
area = calculate_area((5, 10))
print(area)  # Output: 50

#---practice exercises---
#create a tuple of three floats, print each with an index
float_tuple=(3.14, 2.71, 1.61)
print(float_tuple[0])  # Output: 3.14
print(float_tuple[1])  # Output: 2.71
print(float_tuple[2])  # Output: 1.61

#2.given  t=(1,2,[3,4]), append 5 to the list inside the tuplel and print the t.
t=(1,2,[3,4])
t[2].append(5)
print(t)  # Output: (1, 2, [3, 4, 5])

#3.write a function that takes a tuple of numbers and returns a new tuple with each number squared.
def square_tuple(numbers):
    return tuple(x**2 for x in numbers)
result=square_tuple((1, 2, 3, 4))
print(result)  # Output: (1, 4, 9, 16)  

#4.write a function that takes two tuples and returns a new tuple that is the concatenation of the two.
def concatenate_tuples(t1, t2):
    return t1 + t2
result=concatenate_tuples((1, 2), (3, 4))
print(result)  # Output: (1, 2, 3, 4)

#5.write a function that takes a tuple and an element, and returns the index of the element in the tuple or -1 if not found.
def find_index(t, element):
    try:
        return t.index(element)
    except ValueError:
        return -1
result=find_index((10, 20, 30, 40), 30)
print(result)  # Output: 2
result=find_index((10, 20, 30, 40), 50)
print(result)  # Output: -1

#another problem


