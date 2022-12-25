from turtle import Turtle
import time

FONT = ('Courier', 24, 'normal')
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SEGMENT_SHAPE = 'square'
SEGMENT_COLOR = 'white'
HEAD_SHAPE = 'square'
HEAD_COLOR = 'white'


class Snake:

    def __init__(self):
        self.timer = Turtle()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape(HEAD_SHAPE)
        # self.head.color(HEAD_COLOR)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend_position(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.begin_fill()
        new_segment.shape(SEGMENT_SHAPE)
        new_segment.fillcolor(SEGMENT_COLOR)
        new_segment.end_fill()
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # moving snakes body
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def countdown(self):
        self.timer.hideturtle()
        self.timer.color('white')
        self.timer.penup()
        self.timer.goto(0, 150)
        for count in range(3, 0, -1):
            self.timer.clear()
            self.timer.write(f'{count}..', align='center', font=FONT)
            time.sleep(0.5)
        self.timer.clear()
        self.timer.write(arg="GO", align='center', font=FONT)
        time.sleep(0.5)
        self.timer.clear()
