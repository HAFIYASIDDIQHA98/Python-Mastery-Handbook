text = input("Enter sentence: ").lower().split()
freq = {word: text.count(word) for word in set(text)}
print("Frequency:", freq)
