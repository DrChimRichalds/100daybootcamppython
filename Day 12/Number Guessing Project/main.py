
import random
import sys
import sys
import art

print(art.logo)
print('Welcome to the Number Guessing Game! \n I\'m thinking of a number between 1 and 100.')
NUMBER = random.choice(range(1,100))
print(NUMBER)

DIFFICULTY = (input('How hard should the game be? Type Hard or Easy')).lower()
LIVES=0

def guess_game(DIFFICULTY,NUMBER):
    if DIFFICULTY == "hard":
        lives=5
    elif DIFFICULTY == "easy":
        lives= 10
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        if guess == NUMBER:
            print(f"You got it! The answer was {NUMBER}")
            sys.exit(0)
        elif guess > NUMBER:
            print("Too high.")
            lives -= 1
        elif guess < NUMBER:
            print("Too low")
            lives -= 1

    print("You've run out of guesses. Refresh the page to run again.")

guess_game(DIFFICULTY,NUMBER)
