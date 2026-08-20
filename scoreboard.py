from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.lives = 3

        try:
            with open("highscore.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0

        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-230, 270)
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.goto(-70, 270)
        self.write(f"High Score: {self.high_score}", align="left", font=FONT)
        self.goto(230, 270)
        self.write(f"Lives: {self.lives}", align="right", font=FONT)


    def lose_life(self):
        self.lives -= 1


    def check_highscore(self):
        if self.score > self.high_score:
            with open("highscore.txt", "w+") as file:
                file.write(f"{self.score}")
