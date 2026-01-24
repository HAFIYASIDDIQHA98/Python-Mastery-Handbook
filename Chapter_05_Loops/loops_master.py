# ==========================================
# CHAPTER 05: LOOPS (FOR & WHILE)
# ==========================================

# 1. FOR LOOP: Iterating over a range (HackerRank Basics)
print("--- Range Loop ---")
for i in range(1, 6): # 1 se 5 tak chalega
    print(f"Number: {i}")

# 2. ITERATING OVER DATA (Advanced S1 Style)
# Problem: Find employees who have 'Python' in their skill list
employees = [
    {"name": "Ali", "skills": ["Java", "C++"]},
    {"name": "Hafiya", "skills": ["Python", "SQL"]},
    {"name": "Zane", "skills": ["Python", "Excel"]}
]

print("\n--- Searching in Nested Data ---")
python_devs = []
for emp in employees:
    # Checking inside the nested list
    if "Python" in emp["skills"]:
        python_devs.append(emp["name"])

print(f"Python Developers Found: {python_devs}")

# 3. WHILE LOOP: Based on a Condition
print("\n--- While Loop ---")
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1  # This is crucial, otherwise it becomes an infinite loop

# 4. BREAK & CONTINUE
print("\n--- Break and Continue ---")
nums = [1, 2, 3, 4, 5, 6, 7, 8]
for n in nums:
    if n == 3:
        continue # Skip 3
    if n == 6:
        break    # Stop the loop at 6
    print(f"Current Num: {n}")
