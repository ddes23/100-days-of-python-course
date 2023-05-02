from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Scoreboard
from pygame import mixer

screen = Screen()
screen.setup(width=800, height=700)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Why Did It Have To Be Snakes?") 

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

mixer.init()
eat_sound = mixer.Sound('eat_sound.mp3')
mixer.music.load("bg_music.mp3")
mixer.music.play(-1)

def game_over():
    mixer.music.stop()
    mixer.music.load("game_over.mp3")
    mixer.music.play()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    #Detect Collision with Food. 
    if snake.head.distance(food) < 15:
        eat_sound.play()
        food.refresh()
        scoreboard.add_point()
        snake.extend()

    #Detect Collision with Wall.
    if snake.head.xcor() > 400 or snake.head.xcor() < -400 or snake.head.ycor() > 350 or snake.head.ycor() < - 350:
        game_is_on = False
        scoreboard.game_over()
    
    #Detect Collision with Tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            
game_over()           

  
screen.exitonclick()