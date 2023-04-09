# enemies = "Skeleton"

# def increase_enemies():
#     enemies = "Zombie"
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# #bad practice to name your global and local variable the same thing

# enemies = 1

# def increase_enemies():
#     #you have explicit state global, but can be prone to creating bugs and errors. Suggested to use sparingly
#     global enemies
#     enemies += 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#Could use return statements instead
enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants - turn it into all upper case

PI = 3.14159
URL = "www.google.com"


