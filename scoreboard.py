from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 270)
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.goto(-70, 270)
        self.write(f"High Score: {self.high_score}", align="left", font=FONT)
        self.goto(230, 270)
        self.write(f"Lives: {self.lives}", align="right", font=FONT)

