def is_palindrome(text):
    # Cleaning the string: remove spaces and make lowercase
    clean_text = "".join(text.split()).lower()
    # Logic: compare a string with its reverse
    return clean_text == clean_text[::-1]

# Testing
words = ["Racecar", "Python", "Aba", "Hafiya"]
for w in words:
    print(f"Is '{w}' a palindrome? {is_palindrome(w)}")
