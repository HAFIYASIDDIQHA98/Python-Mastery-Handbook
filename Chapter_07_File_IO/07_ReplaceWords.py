# Finding and replacing text in a file
with open("sample.txt", "r") as f:
    content = f.read()

new_content = content.replace("donkey", "######") # Censoring words

with open("sample.txt", "w") as f:
    f.write(new_content)

