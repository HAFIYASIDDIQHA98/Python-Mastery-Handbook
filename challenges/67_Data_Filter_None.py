# Task 67: Removing Missing Values
raw_data = [10, None, 20, 30, None, 50]

# filter(None, list) automatically removes None/False values
clean_data = list(filter(None, raw_data))

print(f"Original: {raw_data}")
print(f"Cleaned: {clean_data}")
