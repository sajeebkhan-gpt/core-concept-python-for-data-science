# what is set in python
'''A set is an unordered collection of unique items in python.Set are mutable which means that
we can add or remove items from a set after its creation. sets are commonly used for membershio 
testing and eliminating duplicate entries from a collection.

difference between list and set
# list is ordered and allows duplicate elements, while set is unordered and only allows unique elements.
difference between tuple and set
# tuple is ordered and immutable, while set is unordered and mutable.'''

#Creating a set
my_set = {1, 2, 3, 'hello', True}
print(my_set)
#another way to create a set using set() function
another_set=set=([4,5,6,'world',False])
print(another_set)
#empty set
'''empty_set = set()
print(type(empty_set))  # Output: <class 'set'>
'''
#adding elements to a set
my_set.add(10)
print(my_set)
my_set.add('python')
print(my_set)

fruits={'apple', 'banana', 'cherry'}
fruits.add('orange')
print(fruits)
fruits.add('banana')  # Adding a duplicate element
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

#updating a set with multiple elements
#update() method can take an iterable (like list, tuple, or another set) as an argument
fruits={'apple', 'banana'}
fruits.update(['cherry', 'date', 'fig'])
fruits.update(('grape', 'honeydew'))
fruits.update({'kiwi', 'lemon'})
print(fruits)

#removing elements from a set
#Three ways to remove elements: remove(), discard(), pop()
my_set={'apple', 'banana', 'cherry'}
my_set.remove('banana')  # Raises KeyError if 'banana' not found
print(my_set)
my_set.discard('cherry')  # Does not raise an error if 'cherry' not found
print(my_set)
my_set.pop()  # Removes and returns an random element    
print(my_set)

#clearing and deleting a set
fruits={'apple', 'banana', 'cherry'}
fruits.clear()
print(fruits)# Output: set()
del fruits #deletes the entire set
# print(fruits)  # This will raise a NameError since 'fruits' is deleted

#set operations
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
#union
union_set = setA.union(setB)
print(f"unions:{union_set}")  # Output: {1, 2, 3, 4, 5, 6}

#intersection
intersection_set = setA.intersection(setB)
print(f"intersection:{intersection_set}")  # Output: {3, 4}

#difference
difference_set = setA.difference(setB)
print(f"difference:{difference_set}")  # Output: {1, 2}

#symmetric difference
symmetric_difference_set = setA.symmetric_difference(setB)  
print(f"symmetric difference:{symmetric_difference_set}")  # Output: {1, 2, 5, 6}

# membeship testing
my_set={1, 2, 3, 'hello'}
print(2 in my_set)  # Output: True
print('world' in my_set)  # Output: False
print(5 not in my_set)  # Output: True
print('hello' not in my_set)  # Output: False

# iterating through a set
colors={'red', 'green', 'blue'}
for color in colors:
    print((color))# Output: red green blue (order may vary)
    
# set comprehension
squared_set={x**2 for x in range(1, 6)}
print(squared_set)  # Output: {1, 4, 9, 16, 25}
# Output: {1, 4, 9, 16, 25}
even_set={x for x in range(1,11) if x%2==0}
print(even_set)  # Output: {2, 4, 6, 8, 10}
# Output: {2, 4, 6, 8, 10}

#frozenset
'''A frozenset is an immutable version of a set, 
meaning that once it is created, its elements cannot be changed.'''
frozen_set = frozenset([1, 2, 3, 'hello'])
print(frozen_set)
#frozen_set.add(4)  # This will raise an AttributeError since frozenset is immutable
print(2 in frozen_set)  # Output: True  
print('world' in frozen_set)  # Output: False
# Output: True
# Output: False

#advantages of using sets
'''1. Uniqueness: Sets automatically handle duplicate values, ensuring that all elements are unique'''
'''2. Membership Testing: Sets provide efficient membership testing, making it faster to check if an element exists in the collection.'''
'''3. Set Operations: Sets support mathematical set operations like union, intersection, difference, and symmetric difference, which can be useful in various applications.'''
'''4. Performance: Sets are implemented using hash tables, which provide average O(1) time complexity for add, remove, and membership testing operations.'''
#disadvantages of using sets
'''1. Unordered: Sets do not maintain the order of elements, which can be a drawback if the order is important for your application.'''
'''2. Mutable Elements Not Allowed: Sets can only contain immutable (hashable) elements, so you cannot include lists or dictionaries as elements in a set.'''
'''3. Memory Overhead: Sets may use more memory compared to other data structures like lists or tuples due to their underlying hash table implementation.'''

#practice problems
'''1. Create a set of your favorite fruits and add a new fruit to the set.'''
'''2. Given two sets, find their union, intersection, and difference.'''
'''3. Write a function that takes a list as input and returns a set containing only the unique elements from the list.'''
'''4. Create a frozenset from a list of numbers and demonstrate that it is immutable by attempting to add an element to it.'''
#solutions
#1. 
favorite_fruits = {'apple', 'banana', 'cherry'}
favorite_fruits.add('orange')
print(favorite_fruits)
#2.
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
print(f"Difference: {difference_set}")
#3.
def unique_elements(input_list):
    return set(input_list)
sample_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = unique_elements(sample_list)
print(unique_set)  # Output: {1, 2, 3, 4, 5}
#4.
numbers = [1, 2, 3, 4, 5]
frozen_numbers = frozenset(numbers)
print(frozen_numbers)

# frozen_numbers.add(6)  # This will raise an AttributeError
print(3 in frozen_numbers)  # Output: True

# Output: frozenset({1, 2, 3, 4, 5})
print(3 in frozen_numbers )  # Output: True



