#There is no such thing as block scope in Python

# game_level = 3
# enemies = ["Skeleton", "Aliens", "Zombies"]

# if game_level < 5:
#     new_enemy = enemies[0]

print(new_enemy)

#If the same code is embedded in a function. 
#If you create a variable within a function, it's only within that function
#But if you create a new variable within a for loop, if statement, while loop it does not create a local scope

game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Aliens", "Zombies"]
    if game_level < 5:
        new_enemy = enemies[0]

print(new_enemy)