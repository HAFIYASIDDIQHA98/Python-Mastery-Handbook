# Task 76: Calculating Percentage Share
# Useful for Budgeting or Data Analysis

expenses = [500, 1200, 300, 1000, 500] # Example: Grocery, Rent, Bills, etc.
total = sum(expenses)

print(f"Total Expenditure: {total}")
print("--- Percentage Share ---")

for item in expenses:
    percent = (item / total) * 100
    print(f"Value {item}: {percent:.2f}%")

# .2f means keeping only 2 digits after the decimal point
