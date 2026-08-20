from turtle import Turtle

class Brick(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.shapesize(stretch_len=1, stretch_wid=2)
        self.color("red")
        self.value = 40

