#Mini project 1:copy contents of One File to Another 
#Goal:Copy all text fromm source.txt into  a new file destination.txt
try:
    with open("source.txt","r") as src:
        content=src.read()

        with open("destination.txt","w") as dest:
            dest.write(content)
            print("File copied successfully!")
except FileNotFoundError:
    print("source file not found!")
except Exception as e:
    print(f"An unexpected error occours:{e}")
          