# Task 70: Basic Outlier Check
ages = [22, 25, 21, 150, 24, 23] # 150 is clearly an outlier

for a in ages:
    if a > 100:
        print(f"Outlier detected: {a}")
