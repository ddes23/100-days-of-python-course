enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope - exists within functions

def drink_potion():
    potion_strentgh = 2
    print(potion_strentgh)

drink_potion()

#Below results in the name error because potion_strength isn't defined outside the function
# print(potion_strength)

#Global Scope - where you define your functions. Variables defined at top level, are available anywhere. 
player_health = 10 

def drink_potion():
    potion_strentgh = 2
    print(player_health)

drink_potion()

#Global and local scope doesn't apply to just variables, but functions and anything you name. 
#This is the concept of namespace. When you name something you need to be mindful of your indentation. 
