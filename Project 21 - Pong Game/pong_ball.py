import random
from turtle import Turtle

BALL_WIDTH = 20
BALL_HEIGHT = 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.width = BALL_WIDTH
        self.height = BALL_HEIGHT
        self.x = 0
        self.y = 0
        self.x_move = 10
        self.y_move = 10

        self.shape("circle")
        self.color("red")
        self.shapesize(self.height/20, self.width/20)
        self.penup()
        self.goto(self.x, self.y)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
