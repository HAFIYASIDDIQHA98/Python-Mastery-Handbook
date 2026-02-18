sentence = "Python development is an amazing career choice"
words = sentence.split()
longest = max(words, key=len)
print(f"Longest word: {longest}")
