import random
import os
from art import logo, vs
from game_data import data

def clear():
    os.system('clear')

def compare_followers(A, B):
    if A > B:
        return "A"
    else:
        return "B"

def first_round():
    global score
    global option_a
    option_b = random.choice(data)
    print(logo)
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

    user_choice = input("\nWho has more followers? Type 'A' or 'B': ")
    correct_choice = compare_followers(option_a['follower_count'], option_b['follower_count'])

    if user_choice == correct_choice and user_choice == "A":
        score += 1
        clear()
        other_rounds()
    elif user_choice == correct_choice and user_choice == "B":
        score += 1
        option_a = option_b
        clear()
        other_rounds()
    else:
        end_game()

def other_rounds():
    global game_over
    global score
    global option_a
    option_b = random.choice(data)
    print(logo)
    print(f"You're right! Current Score: {score}")
    print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
    print(vs)
    print(f"Against B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")

    user_choice = input("\nWho has more followers? Type 'A' or 'B': ")
    correct_choice = compare_followers(option_a['follower_count'], option_b['follower_count'])

    if user_choice == correct_choice and user_choice == "A":
        score += 1
        clear()
    elif user_choice == correct_choice and user_choice == "B":
        score += 1
        option_a = option_b
        clear()
    else:
        clear()
        game_over = True
def end_game():
    global score
    print(logo)
    print(f"Sorry, that's wrong! Final Score: {score}")


def play_game():
    first_round()
    while game_over == False:
        other_rounds()
    end_game()

option_a = random.choice(data)
game_over = False
score = 0

play_game()