# ======================================================
# CHAPTER 01: VARIABLES & DATA TYPES (THE FOUNDATION)
# ======================================================

# 1. VARIABLES & NAMING CONVENTIONS
name = "Hafiya"       # String (str)
age = 22              # Integer (int)
salary = 45000.50     # Floating point (float)
is_developer = True   # Boolean (bool)

print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")

# 2. TYPE CONVERSION (Changing one type to another)
# Very important for handling Input from users
age_str = "25"
age_int = int(age_str)  # String to Integer
print(f"Converted Age: {age_int + 5}") # Now we can do math

# 3. USER INPUT
# input() always returns a string
user_city = "Hyderabad" # Simulation of input
print(f"Candidate Location: {user_city}")

# 4. BASIC OPERATORS
a = 10
b = 3
print(f"Addition: {a + b}")
print(f"Division (Float): {a / b}")
print(f"Division (Integer/Floor): {a // b}") # Removes decimals
print(f"Remainder (Modulus): {a % b}")        # Useful for even/odd check
