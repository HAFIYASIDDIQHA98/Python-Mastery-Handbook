# Finding if a word exists in a file
word = "Python"
with open("sample.txt", "r") as f:
    content = f.read()

if word in content:
    print(f"Yes, '{word}' is present.")
else:
    print(f"No, '{word}' is not found.")
