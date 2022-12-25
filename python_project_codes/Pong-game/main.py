from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
import boundary

NORMAL_DELAY = 0.05
DELAY_REDUCTION_FACTOR = 0.01
WIDTH = 800
HEIGHT = 600

screen = Screen()
boundary.create_boundary(WIDTH, HEIGHT)
screen.listen()
screen.tracer(0)
screen.setup(width=WIDTH+50, height=HEIGHT+50)
screen.bgcolor('black')
screen.title('Pong-game')

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
time.sleep(1)

screen.onkey(fun=right_paddle.up, key="Up")
screen.onkey(fun=right_paddle.down, key="Down")
screen.onkey(fun=left_paddle.up, key="w")
screen.onkey(fun=left_paddle.down, key="s")

score = Scoreboard()

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (320 < ball.xcor() < 361 and ball.distance(right_paddle.pos()) < 50) or \
            (-320 > ball.xcor() > -361 and ball.distance(left_paddle.pos()) < 50):
        ball.bounce_x()

        while (320 < ball.xcor() < 361 and ball.distance(right_paddle.pos()) < 50) or \
                (-320 > ball.xcor() > -361 and ball.distance(left_paddle.pos()) < 50):

            # time.sleep(ball.move_speed)
            ball.move()
            screen.update()

    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()
        right_paddle.reset_position()
        left_paddle.reset_position()
        screen.update()
        time.sleep(1)

    elif ball.xcor() < -380:
        score.r_point()
        ball.reset_position()
        right_paddle.reset_position()
        left_paddle.reset_position()
        screen.update()
        time.sleep(1)

    ball.move()
    screen.update()

screen.exitonclick()
