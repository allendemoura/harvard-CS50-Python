import random, sys

while True:
    level = input("Level: ")
    if level.isnumeric() and "." not in level and int(level) > 0:
        level = int(level)
        break

num = random.randrange(level + 1)

while True:
    guess = input("Guess: ")
    if guess.isnumeric() and "." not in guess and int(guess) > 0:
        guess = int(guess)
        if guess < num:
            print("Too Small!")
        elif guess > num:
            print("Too large!")
        else:
            print("Just right!")
            break

