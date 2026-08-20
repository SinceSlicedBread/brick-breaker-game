from turtle import Turtle

class Paddle(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.setheading(180)
        self.speed("fast")
        self.goto(0, -260)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.x_move = 30


    def move_right(self):
        if self.xcor() < 210:
            self.back(self.x_move)


    def move_left(self):
        if self.xcor() > -210:
            self.forward(self.x_move)
