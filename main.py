from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=500, height=600,starty=10)
screen.bgcolor("black")
screen.title("Arcanoid!")
screen.tracer(0)

game_is_on = True

screen.listen()
paddle = Paddle()

screen.onkey(paddle.move_right, "Right")
screen.onkey(paddle.move_left, "Left")

while game_is_on:
    screen.update()

screen.exitonclick()
