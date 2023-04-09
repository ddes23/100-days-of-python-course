# import another_module
# from turtle import Turtle, Screen

# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("darkGreen")
# timmy.forward(distance=100)
# my_screen.exitonclick()
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["Charmander", "Squirtle", "Bulbasaur", "Pikachu"])
table.add_column("Type", ["Fire", "Water", "Grass", "Electric"])

table.align = "l"

print(table)



