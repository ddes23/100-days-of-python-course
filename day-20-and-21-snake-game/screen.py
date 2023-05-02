from turtle import Screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCREEN_BGCOLOR = "black"

class Snake_Screen():

    def __init__(self):
        self = Screen()
        self.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.bgcolor(SCREEN_BGCOLOR)
        self.tracer(0)
        self.title("Why Did It Have To Be Snakes?")
        self.exitonclick()
    

    

