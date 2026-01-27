def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Printing first 10 numbers of Fibonacci
print("Fibonacci Sequence:")
for i in range(10):
    print(fibonacci(i), end=" ")
