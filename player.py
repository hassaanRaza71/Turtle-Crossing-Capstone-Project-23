from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.restart()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    
    def restart(self):
        self.goto(STARTING_POSITION)