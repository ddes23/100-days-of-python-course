from turtle import Turtle, Screen

screen = Screen()
leo = Turtle()

def move_forwards():
    leo.forward(10)

screen.listen()
screen.onkey(move_forwards, "space")

screen.exitonclick()