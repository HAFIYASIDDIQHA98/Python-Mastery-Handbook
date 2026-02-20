import random
words = ["python", "data", "mysql", "github"]
secret = random.choice(words)
guess = input("Guess the word (python/data/mysql/github): ")

if guess.lower() == secret:
    print("You Won! The word was", secret)
else:
    print("Wrong! The secret word was", secret)
