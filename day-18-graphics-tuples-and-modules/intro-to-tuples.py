import turtle as t
import random

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r, g, b)
    return rgb

direction = [0, 90, 180, 270]        

leo = t.Turtle()
leo.shape('turtle')
leo.pensize(15)
leo.speed(5)

for _ in range(200):
    leo.color(random_color())
    leo.forward(30)
    leo.setheading(random.choice(direction))
   
screen = t.Screen()
screen.exitonclick()
