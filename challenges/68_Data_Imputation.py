# Task 68: Filling gaps in data
data = [5, None, 15, None, 25]

# Using a list comprehension to replace None with 0
filled_data = [x if x is not None else 0 for x in data]

print(f"Filled Data: {filled_data}")
