#mini project 2. Count the Number of words in  a file
#Goal:open a file and count how many words are inside it.
try:
    with open("hello.txt","r") as file:
        text=file.read()
        words=text.split()
        print(f"total number of words:{len(words)}")
except FileNotFoundError:
    print("file not found")
