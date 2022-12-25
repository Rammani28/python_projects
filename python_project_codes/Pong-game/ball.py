from turtle import Turtle

BALL_MOVE_PER_X_FRAME = 2
BALL_MOVE_PER_Y_FRAME = 2
MOVE_SPEED = 0.01  # Starting speed should be 0.01 for move distance = 2 per frame
MAX_SPEED = 0.0019
SPEED_REDUCTION_FACTOR = 0.95


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.y_val = BALL_MOVE_PER_Y_FRAME
        self.x_val = BALL_MOVE_PER_X_FRAME
        self.move_speed = MOVE_SPEED

        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)

    def bounce_x(self, bounce_distance=BALL_MOVE_PER_X_FRAME):
        self.x_val *= -1
        if self.move_speed > MAX_SPEED:
            self.move_speed = round(self.move_speed * SPEED_REDUCTION_FACTOR, 7)
        else:
            if self.move_speed - 0.0001 > 0:
                self.move_speed = round(self.move_speed - 0.0001, 7)
        print(self.move_speed)

    def bounce_y(self):
        self.y_val *= -1

    def move(self):
        new_x = self.xcor() + self.x_val
        new_y = self.ycor() + self.y_val
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = MOVE_SPEED
