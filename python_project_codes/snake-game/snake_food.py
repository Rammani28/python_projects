from turtle import Turtle
import random

WIDTH = 600
HEIGHT = 600
# GRID_ROW = int(WIDTH/40 - 1)      #  for food to be put using grid technique only
# GRID_COLUMN = int(HEIGHT/40 - 1)
# GRID_SIZE = 20

FOOD_COLORS_LIST = ['red', 'violet', 'blue', 'green', 'white']
FOOD_COLOR = FOOD_COLORS_LIST[0]

FOOD_SHAPES_LIST = ['circle', 'turtle', 'square']
FOOD_SHAPE = FOOD_SHAPES_LIST[0]


class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape(FOOD_SHAPE)
        self.color(FOOD_COLOR)
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)  # real_size * 0.8
        self.speed('fastest')
        self.penup()
        self.refresh()

    def refresh(self):
        # grid method puts foods at exact coordinates which are multiple of 20, it works, but it reduced the fun
        # random_x = random.randint(-GRID_ROW, GRID_ROW) * GRID_SIZE
        # random_y = random.randint(-GRID_COLUMN, GRID_COLUMN) * GRID_SIZE
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
