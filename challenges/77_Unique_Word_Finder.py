text = "learning python is fun and learning data science is also fun"
words = text.split()
unique_words = set(words) # Sets automatically remove duplicates

print(f"Original Text: {text}")
print(f"Unique Vocabulary: {unique_words}")
