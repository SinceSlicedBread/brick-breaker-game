from turtle import Screen
import random
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=500, height=600,starty=10)
screen.bgcolor("black")
screen.title("Arcanoid!")
screen.tracer(0)

game_is_on = True

screen.listen()
scoreboard = Scoreboard()
paddle = Paddle()
ball = Ball()

ball.find_paddle(paddle)
## improve ball direction starting options later
#ball.set_ball_direction(random.choice((45, 135)))
ball.set_ball_direction(45)

screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")

while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move_ball()

    print(ball.heading())

    ## detect collision with either side wall and bounce off
    if  ball.xcor() > 230 or ball.xcor() < -230:
        ball.bounce_x(ball.heading())

    ## detect collision with back wall and bounce off
    if ball.ycor() > 280:
        ball.bounce_y(ball.heading())

    ## detect collision with paddle and bounce off
    if ball.distance(paddle) < 30:
        ball.bounce_y(ball.heading())



screen.exitonclick()
