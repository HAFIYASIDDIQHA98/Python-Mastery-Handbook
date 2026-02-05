
sentence = input("Enter a sentence: ")
words = sentence.split()
longest = max(words, key=len)

print(f"The longest word is: {longest}")
print(f"Length: {len(longest)}")
