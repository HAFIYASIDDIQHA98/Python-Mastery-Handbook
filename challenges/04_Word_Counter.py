def count_words():
    text = input("Enter a sentence: ").lower()
    words = text.split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    print("\nWord Frequency:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

count_words()
