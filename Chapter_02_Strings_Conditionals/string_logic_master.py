# ======================================================
# CHAPTER 02: STRINGS & CONDITIONAL STATEMENTS (MASTER)
# ======================================================

# 1. STRING METHODS (The Essentials)
message = "  learning python for FactSet  "

print("Original:", message)
print("Stripped & Upper:", message.strip().upper())
print("Title Case:", message.strip().title())
print("Replace word:", message.replace("learning", "Mastering"))

# 2. SLICING (Accessing parts of strings)
# Syntax: [start: stop: step]
word = "SoftwareEngineer"
print("First 8 chars:", word[:8])     # Software
print("Last 8 chars:", word[8:])      # Engineer
print("Reverse string:", word[::-1])  # reenignEerawtfoS

# 3. CONDITIONAL LOGIC (Decision Making)
marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
else:
    grade = "C"

print(f"Marks: {marks}, Final Grade: {grade}")

# 4. NESTED CONDITIONS (FactSet Logic Style)
is_citizen = True
age = 21

if is_citizen:
    if age >= 18:
        print("Status: Eligible for Professional Role")
    else:
        print("Status: Eligible for Internship")
