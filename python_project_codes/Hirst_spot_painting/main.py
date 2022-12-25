import turtle
from turtle import Turtle, Screen
import random

# import colorgram
#
#
# def color_extractor(no_of_color):
#     extracted_colors = []
#     colors = colorgram.extract("image.jpg", no_of_color)
#
#     for n in range(no_of_color):
#         color = tuple(colors[n].rgb)
#         extracted_colors.append(color)
#     return extracted_colors
#
#
# color_list = color_extractor(26)
# print(color_list)


benny = Turtle()
benny.penup()
benny.hideturtle()
x = -250
y = -250
benny.goto(x, y)
benny.speed('fastest')
turtle.colormode(255)
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53),
              (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48),
              (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155),
              (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120)]


# benny.shape('arrow')
# benny.home()
number_of_dots = 100
for dot_number in range(1, number_of_dots+1):
    benny.dot(20, random.choice(color_list))
    benny.penup()
    benny.forward(50)
    if dot_number % 10 == 0:
        y += 50
        benny.goto(x, y)


screen = Screen()
screen.exitonclick()
