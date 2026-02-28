# Task 81: Equality vs Identity
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b: {a == b}")  # True: because values are same
print(f"a is b: {a is b}")  # False: because they are different objects in memory
print(f"a is c: {a is c}")  # True: because they point to the same memory location
