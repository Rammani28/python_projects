# took 5.5 hours to complete it even with help of instructor
from turtle import Screen
import time
from snake import Snake
from snake_food import Food
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600
BOUNDARY_W = 305
BOUNDARY_H = 305
SCREEN_COLOR = 'black'

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(SCREEN_COLOR)
screen.title('Snake Game by Rammani Acharya')
screen.tracer(0)  # turn off animation effect of screen, we need to use update() method to refresh screen

snake = Snake()
food = Food()
score = Scoreboard()
screen.update()
snake.countdown()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.12)
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score += 1
        score.update_score()
        snake.extend_position()

    if snake.head.xcor() > BOUNDARY_W or snake.head.xcor() < -BOUNDARY_W \
            or snake.head.ycor() > BOUNDARY_H or snake.head.ycor() < -BOUNDARY_H:
        snake.reset()
        screen.update()
        snake.countdown()
        score.reset_score()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset()
            screen.update()
            snake.countdown()

screen.exitonclick()
