'''for num in range (1,4):
    print(f"\multiplication table of {num}")
    for i in range (1,11):
        print(f"{num}*{i}={num*i}")'''
#----pattern with numbers---#

'''for i in range (1,6):
    for j in range (1,i+1):
        print(j,end=" ")
    print()'''

#----pattern with stars---#
'''for i in range (1,6):
    for j in range (1,i+1):
        print("*",end=" ")
    print()'''

#----reverse pattern with numbers---#
'''for i in range (5,0,-1):
    for j in range (1,i+1):
        print(j,end=" ")
    print()'''
#----reverse pattern with stars---#
'''for i in range (5,0,-1):
    for j in range (1,i+1):
        print("*",end=" ")
    print()'''

#----right angle triangle pattern---#
'''for i in range (1,6):
    for j in range (5,i,-1):
        print(" ",end=" ")
    for k in range (1,i+1):
        print("*",end=" ")
    print()'''
#---combined menu program---#
'''print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice=int(input("Enter your choice (1-4): "))  
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
if choice==1:
    print(f"{num1}+{num2}={num1+num2}")
elif choice==2:
    print(f"{num1}-{num2}={num1-num2}")
elif choice==3:
    print(f"{num1}*{num2}={num1*num2}")
elif choice==4:
    if num2!=0:
        print(f"{num1}/{num2}={num1/num2}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid choice. Please select a valid option (1-4).")

'''
'''#function with user input
def greet_user(num1,num2):
    if num1>num2:
        return True
    else:
        return False
num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
if num1>num2:
   print(f"you are eligible {num1}")
else:
 print(f"you are not eligble{num2}")

'''#string slicing get substrings
'''#string[start:end:step]
text="this is sajeeb khan"
print(text[0:3])
print(text[5:])
'''''''''
#string methods

'''text="hello world"
print(text.upper())
print(text.lower())
print(text.replace("world","sajeeb"))

print(text.split(" "))
print(text.find("world"))
print(text.startswith("hello")) 
print(text.endswith("khan"))
print(text.count("o"))
print(len(text))
print(text.index("world"))
print(text.capitalize())
print(text.title())
print(text.center(50,"*"))
print(text.strip())
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())
print(text.swapcase())
print(text.partition(" "))
print(text.rpartition(" "))
print(text.zfill(20))
print(text.encode())
print(text.expandtabs())
print(text.format())
print(text.maketrans("h","H"))
print(text.translate(text.maketrans("h","H")))
print(text.removeprefix("hello"))
print(text.removesuffix("world"))
print(text.casefold())
print(text.islower())
print(text.isupper())
print(text.splitlines())
print(text.rsplit(" "))
print(text.join(["hello","world"]))
print(text.replace("o","0"))
print(text.count("l"))
print(text.index("o"))
print(text.rindex("o"))
print(text.partition("o"))
print(text.rpartition("o"))
print(text.ljust(20,"*"))
print(text.rjust(20,"*"))
print(text.zfill(30))
print(text.encode("utf-8"))
print(text.decode("utf-8"))
print(text.format_map({"hello":"hi","world":"earth"}))
print(text.isprintable())
print(text.isascii())
print(text.removeprefix("h"))

print(text.removesuffix("d"))
print(text.translate(str.maketrans("h","H")))

print(text.expandtabs(4))
print(text.split("\n"))
print(text.rsplit("\n"))
print(text.join(["hi","earth"]))
print(text.replace("l","1"))
print(text.count("e"))
print(text.index("e"))
print(text.rindex("e"))
'''
'''#checking in string
text="sajeeb khan"
if "sajeeb" in text:
    print("found")
else:
    print("not found")
   '''
   # string formatting
'''name="sajeeb"
age=22  
print("my name is {} is and my age is {}".format(name,age))
print(f"my name is {name} and my age is {age}")
print("my name is %s and my age is %d"%(name,age))
print("my name is {n} and my age is {a}".format(n=name,a=age))
'''
#---string reverse---#
'''text="sajeeb khan"
reversed_text=text[::-1]
print(reversed_text)
#---string palindrome---#
text="madam"
if text==text[::-1]:
    print("palindrome")

else:
    print("not palindrome")

#---string count vowels and consonants---#
text="sajeeb khan"
vowels="aeiouAEIOU"
vowel_count=0
consonant_count=0
for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count+=1
        else:
            consonant_count+=1
print(f"Vowels: {vowel_count}")
print(f"Consonants: {consonant_count}")

#---string reverse words---#
text="sajeeb khan"
words=text.split()
reversed_words=" ".join(reversed(words))    
print(reversed_words)
#---string unique characters---#
text="sajeeb khan"
unique_chars=set(text)  
print(unique_chars)
#---string character frequency---#

text="sajeeb khan"  
char_frequency={}   

for char in text:
    if char.isalpha():  
        if char in char_frequency:
            char_frequency[char]+=1
        else:
            char_frequency[char]=1  
print(char_frequency)'''

#string menu program
'''print("1. Count Vowels and Consonants\n2. Reverse String\n3. Check Palindrome\n4. Character Frequency") 
choice=int(input("Enter your choice (1-4): "))  
text=input("Enter a string: ")      
if choice==1:
    vowels="aeiouAEIOU"
    vowel_count=0
    consonant_count=0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count+=1
            else:
                consonant_count+=1
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}") 

elif choice==2:
    reversed_text=text[::-1]
    print(f"Reversed String: {reversed_text}")  
elif choice==3:
    if text==text[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
elif choice==4:
    char_frequency={}
    for char in text:
        if char.isalpha():
            if char in char_frequency:
                char_frequency[char]+=1
            else:
                char_frequency[char]=1
    print("Character Frequency:")
    for char, freq in char_frequency.items():
        print(f"{char}: {freq}")
else:       
    print("Invalid choice. Please select a valid option (1-4).")   '''

#list in python
'''a list is an ordered collection of items which can be of different data types, numbers, strings , booleans , or even other lists.
list are mutable, meaning you can change their contents
syntax:
my_list=[items1,items2,items3]'''
'''fruits=["apple","banana","cherry"]
number=[1,2,3,4,5]
mixed_list=["apple",1,2.5,True]
print(fruits)
print(number)
print(mixed_list)

#accessing list items
print(fruits[0])  #first item
print(fruits[1])  #second item
print(fruits[-1]) #last item
print(fruits[-2]) #second last item
print(fruits[0:2]) #slicing
print(fruits[:3])  #slicing from start to index 2
print(fruits[1:])  #slicing from index 1 to end


#list functions methods
fruits.append("orange")  #add item at the end
print(fruits)
fruits.insert(1,"kiwi")  #add item at specific position
print(fruits)
fruits.remove("banana")  #remove specific item
print(fruits)
fruits.pop()  #remove last item
print(fruits)
fruits.sort()  #sort the list
print(fruits)
fruits.reverse()  #reverse the list
print(fruits)
print(len(fruits))  #length of the list
print(fruits.index("cherry"))  #index of specific item
print(fruits.count("apple"))  #count occurrences of specific item
fruits.clear()  #clear the list
print(fruits)

#list operarations
list1=[1,2,3]
list2=[4,5,6]
combined_list=list1+list2  #concatenation
print(combined_list)
repeated_list=list1*3  #repetition
print(repeated_list)
for item in list1:   #iteration
    print(item)

#nested lists
nested_list=[[1,2,3],[4,5,6],[7,8,9]]
print(nested_list[0])  #first sublist
print(nested_list[1][2])  #specific item in sublist
print(nested_list[2][:2])  #slicing sublist
#itearating nested list

#practice problems
#1. Find the largest number in a list
numbers=[3,5,1,8,2]
largest=max(numbers)
print(f"Largest number is: {largest}")
#2. Calculate the sum of all numbers in a list
numbers=[3,5,1,8,2]
total=sum(numbers)
print(f"Sum of all numbers is: {total}")
#3. Count the occurrences of a specific item in a list
fruits=["apple","banana","cherry","apple","kiwi","banana","apple"]
count=fruits.count("apple")
print(f"Occurrences of apple: {count}")
#4. Remove duplicates from a list
numbers=[1,2,2,3,4,4,5]
unique_numbers=list(set(numbers))
print(f"List after removing duplicates: {unique_numbers}")

#5. Reverse a list
numbers=[1,2,3,4,5]
numbers.reverse()
print(f"reversed list: {numbers}")

#6. Sort a list in ascending order
numbers=[5,2,8,1,4]
numbers.sort()
print(f"Sorted list: {numbers}")
#7. Merge two lists into one
list1=[1,2,3]
list2=[4,5,6]
merged_list=list1+list2
print(f"Merged list: {merged_list}")
#8. Find the second largest number in a list
numbers=[3,5,1,8,2]
numbers.sort()
second_largest=numbers[-2]
print(f"Second largest number is: {second_largest}")
#9. Check if a list is empty
my_list=[]
if not my_list:
    print("The list is empty.")
else:
    print("The list is not empty.")

#ESCAPE CHARACTERS IN PYTHON
text="hello\nworld"  #\n for new line
print(text)
text="hello\tworld"  #\t for tab
print(text)
text="he said \"hello\""  #\" for double quote   
print(text)
text='it\'s a beautiful day'  #\' for single quote
print(text)
text="c:\\users\\sajeeb"  #\\ for backslash
print(text)
text="hello\rworld"  #\r for carriage return
print(text)
text="hello\bworld"  #\b for backspace
print(text)
text="hello\fworld"  #\f for form feed
print(text) 

#pracice questions
#! take a string input from user and print it in reverse
user_input=input("enter  a string:")
reversed_input=user_input[::-1]
print(f"reversed string is :{reversed_input}")
#! take a string input from user and count the number of vowels and consonants
user_input=input("enter a strings:")
count_vowels=0
count_constants=0
vowels="aeiouAEIOU"
for char in user_input:
    if char.isalpha():
        if char in vowels:
            count_vowels+=1
        else:
            count_constants+=1
            print(f"number of vowels:{count_vowels }")

#! take a string input from user and check if it is palindrome or not
user_name=input("enter a string:")
if user_name==user_name[::-1]:
    print("palindrome")
else:
    print("not palindrome")

    #remove all space from a string
user_input=input("enter a string:")
no_space_string=user_input.replace(" ","")
print(f"string without spaces:{no_space_string}")

#replace all vowels in a string with *
user_input=input("enter a string:")
vowels="aeiouAEIOU"
for char in user_input:
    if char in vowels:
        user_input=user_input.replace(char,"*")
print(f"string after replacing vowels:{user_input}")

#replace every "a" with "@" in a string
user_input=input("enter a string:")
modified_string=user_input.replace("a","@").replace("A","@")
print(f"modified string:{modified_string}")

#count the number of words in a string
user_input=input("enter a string:")
words=user_input.split()
word_count=len(words)
print(f"number of words:{word_count}")

#find the longest word in a string
user_input=input("enter a string:")
words=user_input.split()
longest_word=max(words,key=len)
print(f"longest word:{longest_word}")
#find the shortest word in a string
user_input=input("enter a string:")     
words=user_input.split()
shortest_word=min(words,key=len)
print(f"shortest word:{shortest_word}")

#count the number of uppercase and lowercase letters in a string
user_input=input("enter a string:")
count_upper=0
count_lower=0
for char in user_input:
    if char.isupper():
        count_upper+=1
    elif char.islower():
        count_lower+=1
print(f"uppercase letters:{count_upper}")
print(f"lowercase letters:{count_lower}")

#convert a string to title case
user_input=input("enter a string:")
title_case_string=user_input.title()
print(f"title case string:{title_case_string}")
#convert a string to camel case
user_input=input("enter a string:")
words=user_input.split()
camel_case_string=words[0].lower()+''.join(word.capitalize() for word in words[1:])
print(f"camel case string:{camel_case_string}")

#list operations
my_list=[]
if not my_list:
    print("The list is empty.")
#list functions methods
numbers=[4,2,8,6,5]
numbers.sort()
print(f"sorted list:{numbers}")
numbers.reverse()
print(f"reversed list:{numbers}")
numbers.append(10)
print(f"list after appending:{numbers}")
numbers.insert(2,15)
print(f"list after inserting:{numbers}")
numbers.remove(5)
print(f"list after removing:{numbers}")
popped_item=numbers.pop()
print(f"popped item:{popped_item}")

#list comprehension
squares=[x**2 for x in range(1,11)] 
print(f"squares of numbers from 1 to 10:{squares}")
'''

#converting between list and string
string_data="hello sajeeb khna"
list_data=string_data.split()
print(f"list data:{list_data}")
converted_string=" ".join(list_data)
print(f"converted string:{converted_string}")

new_list=['h','e','l','l','o']
converted_string=" ".join(new_list)
after_conversion=converted_string.replace(" ","")
print(f"converted string:{after_conversion}")

#practice problems
#1. Find the largest number in a list
numbers=[10,25,5,40,15]
largest_number=max(numbers)
print(f"Largest number is:{largest_number}")
#2. Calculate the sum of all numbers in a list
numbers=[10,25,5,40,15]
total_sum=sum(numbers)
print(f"Sum of all numbers is:{total_sum}")

# create a list of 5 numbers and calcualte the avarage
numbers=[10, 20, 30, 40, 50]  # changed code
total_sum=sum(numbers)
avarage_sum=total_sum/len(numbers)
print(f"avarage of numbers is:{avarage_sum}")

#take a list of numbers and find the even and odd numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=[]
odd_numbers=[]
for num in numbers:
    if num%2==0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
        print(f"even numbers:({even_numbers})")
        print(f"odd numbers:({odd_numbers})")
 #generate a list of squares of numbers from 1 to 10 usig list comprehension
squares=[x**2 for x in range(1,11)]
print(f"squares of numbers from 1 to 10:{squares}")
      
#find the common elements between two lists
list1=[1,2,3,4,5]
list2=[4,5,6,7,8]
common_elements=list(set(list1)&set(list2))
print(f"common elements:{common_elements}")

#remove duplicates from a list while preserving the order
numbers=[1,2,2,3,4,4,5]
unique_numbers=[]
for num in  numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print(f"list after removing duplicates:{unique_numbers}")

#take a list of names print only those starting with 'S'
names=["sajeeb","khan","sara","john","smith"]
for name in names:
    if name.startswith("s") or name.startswith ("S"):
     print(f"name starting with S:{name}")

#---section Tuple in python---
'''A tuple is an ordered collection of items 
which can be of different data types, numbers, strings , booleans ,
or even other tuples.'''