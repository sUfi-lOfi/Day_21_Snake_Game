import time
from turtle import Turtle,Screen
from time import sleep
from snake import Snake
from food import Food


screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor("#000000")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

#---------------Instances---------------#
food = Food()
snake = Snake()
snake.create_snake()
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.06)
    snake.move()
# ---------------Movement Control---------------#
    screen.onkey(key="Left",fun=snake.move_left)
    screen.onkey(key="Right",fun=snake.move_right)
    screen.onkey(key="Up", fun=snake.move_up)
    screen.onkey(key="Down", fun=snake.move_down)
    snake_head_pos = snake.snake_body[0].pos()
    if abs(snake_head_pos[0]) >= 300 or abs(snake_head_pos[1]) >= 300:
        game_is_on = False
    if food.distance(snake.snake_body[0]) < 20:
        food.relocate()
        snake.extend()











screen.exitonclick()