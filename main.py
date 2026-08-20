from turtle import Screen
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
ball.set_ball_direction(45)
wall = []

def create_wall():
    global wall
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
                brick.value = 10
            elif line <= 4:
                brick.color("blue")
                brick.value = 20
            elif line <= 6:
                brick.color("orange")
                brick.value = 30

            wall.append(brick)

        start_y -= 30
        line -= 1
        brick_no = 9
    screen.update()

create_wall()

screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")

while scoreboard.lives >= 0 and scoreboard.score < 1800:
    time.sleep(ball.speed)
    screen.update()
    ball.move_ball()
    ball.detect_collision(ball.xcor(),
                          ball.ycor(),
                          ball.heading(),
                          ball.distance(paddle))

    if scoreboard.score >= 600 and ball.speed == 0.1:
        ball.speed -= 0.03
        paddle.x_move += 5
    elif scoreboard.score >= 1200 and ball.speed == 0.07:
        ball.speed -= 0.02

    if ball.ycor() < -320:
        scoreboard.lose_life()
        scoreboard.update_scoreboard()
        ball.hideturtle()
        del ball
        ball = Ball()
        ball.set_ball_direction(45)
        ball.find_paddle(paddle)

    for brick in wall:
        if ball.distance(brick) <= 20:
            ball.bounce_y(ball.heading())
            brick.goto(1000,1000)
            scoreboard.score += brick.value
            scoreboard.update_scoreboard()

scoreboard.check_highscore()
screen.exitonclick()
