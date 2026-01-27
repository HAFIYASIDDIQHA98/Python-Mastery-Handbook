# ======================================================
# CHAPTER 07: FILE I/O & EXCEPTION HANDLING (MASTER)
# ======================================================

# 1. WRITING TO A FILE
# 'w' mode (write) purana data uda deta hai, 'a' mode (append) naya data jodta hai
content = "Employee Name: Hafiya\nRole: Python Developer\nLocation: Hyderabad"

with open("report.txt", "w") as file:
    file.write(content)
    print("File 'report.txt' successfully created!")

# 2. READING FROM A FILE
try:
    with open("report.txt", "r") as file:
        data = file.read()
        print("\n--- Reading File Content ---")
        print(data)
except FileNotFoundError:
    print("Error: The file you are looking for does not exist.")

# 3. EXCEPTION HANDLING (Try-Except)
# Ye HackerRank ke advanced questions mein bahut kaam aata hai
def safe_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Please provide numbers only."

print("\n--- Testing Exception Handling ---")
print(f"Result 1: {safe_division(10, 2)}")
print(f"Result 2: {safe_division(10, 0)}")
