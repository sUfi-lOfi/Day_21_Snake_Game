from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.relocate()

    def relocate(self):
        rand_x = randint(-280,280)
        rand_y = randint(-280,280)
        self.setposition(rand_x,rand_y)