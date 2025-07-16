from turtle import Turtle
class Snake:
    def __init__(self):
        self.snake_body = []
        self.snake_dir = 0
    def create_snake(self):
        for n in range(3):
            turtle = Turtle()
            turtle.shape("square")
            turtle.penup()
            turtle.color("#FFFFFF")
            turtle.setx(-20*n)
            self.snake_body.append(turtle)
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

