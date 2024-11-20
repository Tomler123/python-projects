from turtle import Turtle
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
HEAD_COLORS = ['red', 'green', 'blue', 'yellow', 'pink']
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.create_snake()
        self.head = self.segments[0]
        self.head.color(random.choice(HEAD_COLORS))
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN and self.segments[0].heading() != UP:
            self.segments[0].setheading(UP)
            self.move()
    def down(self):
        if self.segments[0].heading() != UP and self.segments[0].heading() != DOWN:
            self.segments[0].setheading(DOWN)
            self.move()
    def left(self):
        if self.segments[0].heading() != RIGHT and self.segments[0].heading() != LEFT:
            self.segments[0].setheading(LEFT)
            self.move()
    def right(self):
        if self.segments[0].heading() != LEFT and self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(RIGHT)
            self.move()

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.color(random.choice(HEAD_COLORS))