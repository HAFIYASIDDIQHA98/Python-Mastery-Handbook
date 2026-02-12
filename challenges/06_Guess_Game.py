import random

def start_game():
    secret_number = random.randint(1, 20)
    print("I have picked a number between 1 and 20. Can you guess it?")
    
    attempts = 0
    while True:
        guess = int(input("Your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Correct! You took {attempts} attempts.")
            break

start_game()
