import turtle as t

screen = t.Screen()
leo = t.Turtle()
leo.speed(0)

def move_forward():
    leo.forward(5)

def move_backwards():
    leo.backward(5)

def turn_clockwise():
    leo.right(5)

def turn_counterclockwise():
    leo.left(5)

def reset_screen():
    leo.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=reset_screen)

screen.exitonclick()