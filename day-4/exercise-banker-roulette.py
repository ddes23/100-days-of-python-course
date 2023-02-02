# Instructions

# You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a List called names. 
# For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Where I started
# print(f"{names[random.randint(0,4)]} is going buy the meal today!")

#Angela's suggested solution

num_items = len(names)
random_choice = names[random.randint(0, num_items - 1)]
print(f"{random_choice} will pay for the meal!")

#Then, ultimately revealed it was harder then it needed to be to test conceptually grasp and the choice() function
#would be more efficient