text = "apple banana apple cherry banana apple"
words = text.split()
counts = {w: words.count(w) for w in set(words)}
print("Word Counts:", counts)
