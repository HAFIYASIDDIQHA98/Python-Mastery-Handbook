names = ["Hafiya", "AI", "Python", "DS", "DataScience", "SQL"]

# Filter words that have more than 3 characters
long_names = [n for n in names if len(n) > 3]

print(f"Original List: {names}")
print(f"Filtered (Length > 3): {long_names}")
