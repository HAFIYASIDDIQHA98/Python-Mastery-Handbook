# Program to count total words in a file
with open("sample.txt", "r") as f:
    content = f.read()
    words = content.split()
    print(f"Total words in file: {len(words)}")
