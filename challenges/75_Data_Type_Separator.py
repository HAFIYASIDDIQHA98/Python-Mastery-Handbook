# Task 75: Separating numbers from text
mixed_data = [10, "Apple", 20, "Banana", 30, "Cherry"]

numbers = [x for x in mixed_data if isinstance(x, int)]
text = [x for x in mixed_data if isinstance(x, str)]

print(f"Numbers: {numbers}")
print(f"Text: {text}")
