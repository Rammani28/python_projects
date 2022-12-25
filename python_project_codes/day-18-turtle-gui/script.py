import turtle
from turtle import Turtle, Screen
from random import choice, randint

benny_the_turtle = Turtle()
# benny_the_turtle.shape('turtle')
benny_the_turtle.color('black')


# draw descending maze type of square
# x = 400
# for _ in range(40):
#     benny_the_turtle.forward(x)
#     benny_the_turtle.left(90)
#     x -= 10

# draw a 100 by 100 square at a random position on screen
# for x in range(4):
#     benny_the_turtle.forward(100)
#     benny_the_turtle.left(90)

# Draws a dashed line
# for x in range(50):
#     benny_the_turtle.forward(10)
#     benny_the_turtle.pendown()
#     if x % 2 == 0:
#         benny_the_turtle.penup()

# draws polygons with sides 3 to 10 each with random color
# benny_the_turtle.pensize(10)
# color_list = ['red', 'blue', 'green', 'yellow', 'black', 'purple', 'violet', 'indigo', 'gray', 'brown', 'pink']
# n = 3
# for sides in range(3, 11):
#     benny_the_turtle.pencolor(choice(color_list))
#     for i in range(n):
#         benny_the_turtle.forward(100)
#         benny_the_turtle.right(360 / n)
#     n += 1


# Random walk
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tup = (r, g, b)
    return tup


#
#
turtle.colormode(255)
benny_the_turtle.pensize(2.5)
# angles = [0, 90, 180, 270]
# # color_list = ['red', 'blue', 'green', 'yellow', 'black', 'purple', 'violet', 'indigo', 'gray', 'brown', 'pink']
benny_the_turtle.speed('fastest')


#
# for _ in range(200):
#     benny_the_turtle.setheading(choice(angles))
#     benny_the_turtle.pencolor(random_color())
#     benny_the_turtle.forward(50)

# spirograph

def spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        benny_the_turtle.setheading(benny_the_turtle.heading() + size_of_gap)
        benny_the_turtle.pencolor(random_color())
        benny_the_turtle.circle(200)


spirograph(5)
screen = Screen()
screen.exitonclick()
