import random

true_number = random.randint(1, 20)
guess = 0
guess_count = 0

while guess != true_number:
    guess = int(input("Guess a whole number between 1 and 20: "))
    guess_count += 1
    if guess < true_number:
        print("Too small. Try again.")
    elif guess > true_number:
        print("Too large. Try again.")

print(f"You guessed right!\nTotal guess count: {guess_count}")