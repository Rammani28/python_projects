from turtle import Turtle


def create_boundary(width, height):
    tim = Turtle()
    tim.speed('fastest')
    tim.hideturtle()
    tim.penup()
    tim.color('white')
    tim.goto(width/2, height/2)
    tim.pensize(width=10)
    tim.pendown()

    for _ in range(2):
        tim.right(90)
        tim.forward(height)
        tim.right(90)
        tim.forward(width)



