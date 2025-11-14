#project 3.save user  input into a text file
'''take input from a user aand save it inside a text file named notes.txt. 
if the file is already exist , new input should be added instead of overwriting'''
try:
    user_input=input("Enter your notes:")
    with open("notes.txt","a") as file:
        file.write(user_input  + "\n")
        print("note saved successsfully")
except Exception as e:
    print((f"Error:{e}"))
