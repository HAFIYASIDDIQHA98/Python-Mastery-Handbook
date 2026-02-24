# Task 73: Pairing Data (Names and Scores)
# This is very useful for organizing raw data

names = ["Hafiya", "Python", "Data_Science"]
scores = [95, 88, 92]

# Using zip() to pair elements and dict() to convert to dictionary
data_map = dict(zip(names, scores))

print(f"Names List: {names}")
print(f"Scores List: {scores}")
print(f"Mapped Dictionary: {data_map}")

# Accessing a specific value
print(f"Hafiya's Score: {data_map['Hafiya']}")
