from turtle import Turtle, Screen

tim = Turtle()
tim.speed('fastest')
tim.pensize(2)
screen = Screen()

unit = 20


def move_forward():
    tim.forward(unit)


def move_backward():
    # tim.left(180)
    tim.backward(unit)


angle = 20


def rotate_left():
    tim.left(angle)


def rotate_right():
    tim.right(angle)
    # tim.forward(unit)

def clear_all():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=rotate_right, key='d')
screen.onkey(fun=rotate_left, key='a')
screen.onkey(fun=
             clear_all, key='c')
screen.exitonclick()
