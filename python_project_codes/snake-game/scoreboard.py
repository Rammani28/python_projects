from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # /home/rammani/PycharmProjects/snake-game/main.py
        with open('../../Desktop/high_score.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"score: {self.score} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('../../Desktop/high_score.txt', mode='w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
