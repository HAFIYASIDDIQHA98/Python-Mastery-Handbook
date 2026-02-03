# Program to copy content from one file to another
with open("source.txt", "r") as f1:
    content = f1.read()

with open("destination.txt", "w") as f2:
    f2.write(content)

print("File Copied Successfully!")
