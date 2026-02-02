# Searching line number where a word exists
with open("log.txt", "r") as f:
    lines = f.readlines()

for index, line in enumerate(lines):
    if "Error" in line:
        print(f"Error found on line number: {index + 1}")
