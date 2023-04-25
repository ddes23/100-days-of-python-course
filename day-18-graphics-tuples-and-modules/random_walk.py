from turtle import Turtle, Screen
import random

colors = ["dodger blue", "forest green", "salmon", "orchid3", "purple2", "orange", "yellow", "cyan", "seashell4"
]

direction = ["left", "right"]        

leo = Turtle()
leo.shape('turtle')
leo.pensize(7)
leo.speed(5)

def new_walk(colorchoice):
    leo.color(colorchoice)
    turn = random.choice(direction)
    if turn == "left":
        leo.left(90)
    else:
        leo.right(90)
    leo.forward(50)

running = True

while running:
    new_walk(random.choice(colors))
   
screen = Screen()
screen.exitonclick()
