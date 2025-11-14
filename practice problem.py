#practice 1:Handle file not found error
'''write a program to open a file named "sample.txt" for reading .If the file doesn't exist
 show the custom message:"file not found !please check the filename.'''
try:
    file=open('sample.txt','r')
    content=file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("file not found!please check the filename.")

#practice 2--Handle permission errors
'''try to open a file that you don't have permission to write into, and handle the error gracefully.'''
try:
    file=open('readonly.txt','w')
    file.write("Trying to write something.")
    file.close()

except PermissionError:
    print("you don't have permission to modify this file.")
    

#practice 3--Handle multiple exceptions
'''open a file , read contents and handle both FileNotFoundError and IOError.'''
try:
    file = open("data.txt", "r")
    data = file.read()
    print(data)
except FileNotFoundError:
    print("File does not exist.")
except IOError:
    print("Error while reading the file.")
finally:
    print("File handling complete.")

#practice-4..using with + exception handling
try:
    with open("note.txt","r") as file:
      print(file.read())
      print("operation successfull")
except FileNotFoundError:
      print("file not found")
except Exception as e:
    print(f"an unexpected error occurred:{e}")
#practice -5. combine reading ,writing and exception handling 
'''Ask user for a filename, then try to:
Read its content 
If not found, create a new file and write "This is a new file."'''

filename=input("Enter filename:")
try:
    with open(filename,"r") as f:
        print("file content:")
        print(f.read())
except FileNotFoundError:
 print("file not found!create new one file...")
 with open(filename,"w") as f:
     f.write("this is a new file.")
     print("New file created successfully")



    