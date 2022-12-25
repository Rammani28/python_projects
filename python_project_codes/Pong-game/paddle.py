from turtle import Turtle

PADDLE_UNIT_MOVEMENT = 45


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.penup()
        self.goto(position)
        self.position = position

    def down(self):
        if self.ycor() > -270:
            new_y = self.ycor() - PADDLE_UNIT_MOVEMENT
            self.goto(self.xcor(), new_y)
            # print(self.ycor())

    def up(self):
        if self.ycor() < 270:
            new_y = self.ycor() + PADDLE_UNIT_MOVEMENT
            self.goto(self.xcor(), new_y)
            # print(self.ycor())

    def reset_position(self):
        self.goto(self.position)
