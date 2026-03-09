import random

number = random.randint(1, 100)

print("🎮 Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")

guess = int(input("Enter your guess: "))

while guess != number:

    if guess > number:
        print("Too high!")
    else:
        print("Too low!")

    guess = int(input("Try again: "))

print("🎉 Correct! You guessed the number!")
