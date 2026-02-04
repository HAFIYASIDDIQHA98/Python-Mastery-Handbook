# File: 10_Fibonacci.py
n = 10 # Kitne numbers chahiye
a, b = 0, 1
count = 0

print("Fibonacci Sequence:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
