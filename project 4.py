#project 4.read and display only first 3 lines
#goal:open a file and display only the three lines of text

try:
    with open("story.txt","r") as file:
        for i in range(3):
            line=file.readline()
            if not line:
                break
            print(line.strip())
except FileNotFoundError:
    print("File not found")
