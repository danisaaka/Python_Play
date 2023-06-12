from turtle import Turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_MOVEMENT = 30


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")  # Set the shape of the paddle to a square
        self.color("white")  # Set the color of the paddle to white
        self.shapesize(stretch_wid=(PADDLE_HEIGHT / 20), stretch_len=(PADDLE_WIDTH / 20))  # Set the size of the paddle
        self.penup()
        self.goto(x, y)  # Set the initial position of the paddle

    def move_up(self):
        new_y = self.ycor() + PADDLE_MOVEMENT  # Calculate the new y-coordinate for moving the paddle up
        self.sety(new_y)  # Move the paddle to the new y-coordinate

    def move_down(self):
        new_y = self.ycor() - PADDLE_MOVEMENT  # Calculate the new y-coordinate for moving the paddle down
        self.sety(new_y)  # Move the paddle to the new y-coordinate
