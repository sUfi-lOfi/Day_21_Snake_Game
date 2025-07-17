from turtle import Turtle
from urllib.response import addclosehook


class Snake:
    def __init__(self):
        self.snake_body = []
        self.snake_dir = 0
        self.starting_positions = [(-20,0),(-40,0),(-60,0)]
    def create_snake(self):
        for pos in self.starting_positions:
            self.add_segment(pos)

    def add_segment(self,position):
        turtle = Turtle()
        turtle.shape("square")
        turtle.penup()
        turtle.color("#FFFFFF")
        turtle.goto(*position)
        self.snake_body.append(turtle)
    def extend(self):
        self.add_segment(self.snake_body[-1].pos())
    def move(self):
        for n in range(len(self.snake_body)-1,0,-1):
            cords = self.snake_body[n-1].pos()
            self.snake_body[n].goto(*cords)
        self.snake_body[0].forward(20)
    def move_left(self):
        if self.snake_dir != 0:
            self.snake_body[0].setheading(180)
            self.snake_dir = 180
    def move_right(self):
        if self.snake_dir != 180:
            self.snake_body[0].setheading(0)
            self.snake_dir = 0
    def move_up(self):
        if self.snake_dir != 270:
            self.snake_body[0].setheading(90)
            self.snake_dir = 90
    def move_down(self):
        if self.snake_dir != 90:
            self.snake_body[0].setheading(270)
            self.snake_dir = 270

