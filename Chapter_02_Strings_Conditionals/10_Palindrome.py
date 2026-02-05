# File: 15_Palindrome.py
text = input("Enter a word or number: ").lower()

if text == text[::-1]:
    print("Yes, it is a Palindrome!")
else:
    print("No, it is not a Palindrome.")
