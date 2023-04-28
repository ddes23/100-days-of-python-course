import turtle as t
import random
screen = t.Screen()
t.colormode(255)

color_list = [(75, 180, 58), (143, 93, 64), (184, 145, 103), (32, 126, 37), (36, 82, 179), (20, 92, 32), (7, 65, 8), (105, 195, 95), (164, 128, 77), (80, 54, 19), (216, 199, 141), (141, 218, 134), (84, 70, 24), (99, 48, 37), (117, 158, 208), (200, 231, 217), (175, 104, 90), (233, 213, 179), (215, 142, 153)]

xpos = -300
ypos = -300

leo = t.Turtle()
leo.hideturtle()
leo.penup()
leo.speed(0)

def draw_line():
    global xpos, ypos
    leo.setposition(xpos, ypos)
    for i in range(13):
        leo.dot(20, random.choice(color_list))
        leo.forward(50)
    ypos += 50
        
for i in range(15):
    draw_line()

screen.exitonclick()


