rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_choice = int(input ("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
hands = [rock, paper, scissors]
hand_strings = ["Rock", "Paper", "Scissors"]

print(f"You chose: {hand_strings[user_choice]} \n")
print(hands[user_choice])
print(f"The comptuer chose: {hand_strings[computer_choice]}")
print(hands[computer_choice])

if user_choice == computer_choice:
    print ("You tied")
elif user_choice == 0:
    if computer_choice == 2:
        print("You Win!")
    else:
        print("You Lose")
elif user_choice == 1:
    if computer_choice == 0:
        print("You Win!")
    else:
        print("You Lose")
elif user_choice == 2:
    if computer_choice == 1:
        print("You Win!")
    else:
        print("You Lose")
