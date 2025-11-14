#syntax
'''try:
    # code that may raise exception
except SomeException:
    # handle that exception
except AnotherException as e:
    # handle another exception, 'e' contains info
else:
    # runs if no exception occurred
finally:
    # always runs (cleanup)
'''
#common exceptions in file handling 
'''FileNotFoundError-file path doesn't exist
PermissionError-os denies access 
IsADirectoryError-you tried to open a directory as a FileExistsError
IdError/OsError-general I/O errors
UnicodeDecodeError-reading file with wrong EncodingWarning
ValueError-converting read string to int when its not numeric
'''
#example--1 safe file read(handle missing file)
try:
    with open('data.txt','r') as f:
        content=f.read()
except FileNotFoundError:
    print('Error:permission denied when trying to read "data.txt".')
except Exception as e:
    print("Unexpected error:",e)
else:
    print("file read successfully.first 100 chars:")
    print(content[:100])

#example--handling file not found error 
try:
    f=open('data.txt','r')
    content=f.read()
    print(content)
    f.close()
except FileNotFoundError:
    print("Error:The file 'data.txt' does not exist.")

#example 2:Handling Multiple Errors
try:
    f=open('data.txt','r')
    value=int(f.readline())
    print(value)
except FileNotFoundError:
    print('File not found.')
except ValueError:
    print('Invalid data! could not convert to interger')

#example 3. using else and finally
try:
    f=open('message.txt','r')
except FileNotFoundError:
    print('file not found')
else:
    print('file opended successfully')
    print(f.read())
    f.close()
finally:
    print('program finished running.')

#example Handling unknown errror
try:
    f=open('unknown.txt','r')
    print(f.read())
except Exception as e:
    print(f'an unexpected error occurred:{e}')
