import turtle as t
from tkinter import messagebox
import random


colors = ["blue", "red", "purple", "orange"]
the_boys = []
screen = t.Screen()
y_positions = [-200, -75, 50, 175]
is_race_on = False

screen.setup(width=1000, height=600)

user_bet = screen.textinput("Make your bet!", prompt="Which Turtle will win the race? Enter 'Leo', 'Raph', 'Mikey', or 'Donnie': ")

for i in range(0, 4):
    turt = t.Turtle("turtle")
    turt.color(colors[i])
    turt.shapesize(5, 5)
    turt.penup()
    turt.goto(-400, y_positions[i])
    the_boys.append(turt)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in the_boys:
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == "blue":
                winning_turtle = "Leo"
            elif winning_color == "red":
                winning_turtle = "Raph"
            elif winning_color == "orange":
                winning_turtle = "Mikey"
            elif winning_color == "purple":
                winning_turtle = "Donnie"
            if winning_turtle == user_bet:
                final_message = (f"You won! {winning_turtle} was the winner! ")
            else:
                final_message = (f"Sorry, you lost! {winning_turtle} was the winner! You bet on {user_bet}!")
        
        

        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)


messagebox.showinfo("Results", final_message)
screen.exitonclick()