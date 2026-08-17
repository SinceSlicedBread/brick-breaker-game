from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("turtle")
        self.move_x = 10
        self.move_y = 10
        self.speed = 0.1

    def find_paddle(self, paddle):
        paddle_x, paddle_y = paddle.pos()
        self.goto(paddle_x, paddle_y + 20)


    def set_ball_direction(self, heading):
        self.setheading(heading)


    def move_ball(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_x(self, current_heading):
        if 0 < current_heading < 180:
            new_heading = 180 - current_heading

        elif 180 < current_heading < 360:
            new_heading = 540 - current_heading
        self.setheading(new_heading)
        self.move_x *= -1


    def bounce_y(self, current_heading):
        new_heading = 360 - current_heading
        self.setheading(new_heading)
        self.move_y *= -1


