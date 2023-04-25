from turtle import Turtle, Screen
import random

colors = ["dodger blue", "forest green", "salmon", "orchid3", "purple2", "orange", "yellow", "cyan", "seashell4"
]
leo = Turtle()

leo.shape('triangle')
leo.color("black")

def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        leo.forward(100)
        leo.right(angle)

for sides in range(3,11):
    leo.color(random.choice(colors))
    draw_shape(sides)


screen = Screen()
screen.exitonclick()
