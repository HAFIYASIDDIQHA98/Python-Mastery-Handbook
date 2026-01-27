# ======================================================
# CHAPTER 06: FUNCTIONS & RECURSION (CLEAN & NEAT)
# ======================================================

# 1. BASIC FUNCTION (With Parameters and Return)
# Remember: Return is used to send the result back to the caller
def calculate_tax(salary, tax_rate=0.1):
    """Calculates tax based on salary and rate."""
    tax_amount = salary * tax_rate
    return tax_amount  # This sends the value out of the function

# Calling the function
hafiya_tax = calculate_tax(60000, 0.15)
print(f"Tax to be paid: {hafiya_tax}")

# 2. MULTIPLE RETURN VALUES
# Financial data often needs multiple outputs
def get_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
    avg = total/count
    return total, avg  # Returning a tuple

mysum, myavg = get_stats([10, 20, 30, 40])
print(f"Total: {mysum}, Average: {myavg}")

# 3. RECURSION (Function calling itself)
# Interview Favorite: Factorial or Fibonacci
def factorial(n):
    if n == 1 or n == 0:  # Base Case
        return 1
    else:
        return n * factorial(n - 1) # Recursive Call

print(f"Factorial of 5: {factorial(5)}")

# 4. LAMBDA FUNCTIONS (One-liners)
# Used for quick data processing
square = lambda x: x * x
print(f"Square of 9: {square(9)}")
