from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('digital', 32, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 240)
        self.write(arg=f"{self.l_score}", font=FONT)
        self.goto(100, 240)
        self.write(arg=f"{self.r_score}", font=FONT)

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def l_point(self):
        self.l_score += 1
        self.update_score()
