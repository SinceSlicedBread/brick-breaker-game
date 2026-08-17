from turtle import Screen
import random
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bricks import Brick

screen = Screen()
screen.setup(width=500, height=600,starty=10)
screen.bgcolor("black")
screen.title("Arcanoid!")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
paddle = Paddle()
ball = Ball()

ball.find_paddle(paddle)
## improve ball direction starting options later
#ball.set_ball_direction(random.choice((45, 135)))
ball.set_ball_direction(45)

def create_wall():
    line = 8
    brick_no = 9
    start_y = 250
    while line > 0:
        start_x = -210
        while brick_no > 0:
            brick = Brick()
            brick.goto(start_x, start_y)
            start_x += 50
            brick_no -= 1

            if line <= 2:
                brick.color("green")
            elif line <= 4:
                brick.color("blue")
            elif line <= 6:
                brick.color("orange")



        start_y -= 30
        line -= 1
        brick_no = 9
    screen.update()

create_wall()


screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")

while scoreboard.lives >= 0:
    time.sleep(ball.speed)
    screen.update()
    ball.move_ball()
    ball.detect_collision(ball.xcor(),
                          ball.ycor(),
                          ball.heading(),
                          ball.distance(paddle))
    if ball.ycor() < -320:
        scoreboard.lose_life()
        scoreboard.update_scoreboard()
        ball.hideturtle()
        del ball
        ball = Ball()
        ball.set_ball_direction(45)
        ball.find_paddle(paddle)



screen.exitonclick()
