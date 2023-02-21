import random
import os
from art import logo
def clear():
    os.system('clear')

print(logo)
print("\nWelcome to the Number Guessing Game! ")
game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
all_possible_numbers = list(range(1,101))

if game_difficulty == "easy":
    clear()
    correct_number = random.choice(all_possible_numbers)
    print(f"psst the number is {correct_number}")
    lives = 10
    print("I'm thinking of a number between 1 and 100")
    print(f"You have {lives} attempts left to guess the number.")
    guess = int(input("Make a guess: "))

    while lives > 1:
        if guess > correct_number:
            lives -= 1
            print("Too high.")
            print("Guess again.")
            print(f"You have {lives} attempts remianing to guess the number. ")
            guess = int(input("Make a guess: "))
        elif guess < correct_number:
            lives -= 1
            print("Too low.")
            print("Guess again.")
            print(f"You have {lives} attempts remianing to guess the number. ")
            guess = int(input("Make a guess: "))
        elif guess == correct_number:
            print(f"You got it! the answer was {correct_number}")
            lives = 0
    print("You lose!")
elif game_difficulty == "hard":
    clear()
    correct_number = random.choice(all_possible_numbers)
    print(f"psst the number is {correct_number}")
    lives = 5
    print("I'm thinking of a number between 1 and 100")
    print(f"You have {lives} attempts left to guess the number.")
    guess = int(input("Make a guess: "))

    while lives > 1:
        if guess > correct_number:
            lives -= 1
            print("Too high.")
            print("Guess again.")
            print(f"You have {lives} attempts remianing to guess the number. ")
            guess = int(input("Make a guess: "))
        elif guess < correct_number:
            lives -= 1
            print("Too low.")
            print("Guess again.")
            print(f"You have {lives} attempts remianing to guess the number. ")
            guess = int(input("Make a guess: "))
        elif guess == correct_number:
            print(f"You got it! the answer was {correct_number}")
            lives = 0
    print("You lose!")
    
