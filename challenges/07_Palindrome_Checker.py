def check_palindrome():
    word = input("Enter a word: ").lower()
    if word == word[::-1]:
        print("✅ It's a Palindrome!")
    else:
        print("❌ Not a Palindrome.")

check_palindrome()
