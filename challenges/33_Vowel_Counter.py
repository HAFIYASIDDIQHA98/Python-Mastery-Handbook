text = input("Enter text: ").lower()
count = sum(1 for char in text if char in "aeiou")
print(f"Number of vowels: {count}")
