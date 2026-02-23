# Task 71: Cleaning extra spaces from data
dirty_names = ["  Hafiya", "Python  ", "  Data Science  ", " Machine Learning "]

# strip() removes spaces from both ends
clean_names = [name.strip() for name in dirty_names]

print(f"Original: {dirty_names}")
print(f"Standardized: {clean_names}")
