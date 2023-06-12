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
        self.x_move = random.choice([-10, 10])  # Set the initial x movement randomly to the left or right
        self.y_move = random.choice([-10, 10])  # Set the initial y movement randomly up or down
        self.move_speed = 0.1  # Set the initial movement speed

        self.shape("circle")  # Set the shape of the ball to a circle
        self.color("red")  # Set the color of the ball to red
        self.shapesize(self.height/20, self.width/20)  # Set the size of the ball
        self.penup()
        self.goto(self.x, self.y)  # Set the initial position of the ball
        self.collided = False  # Flag to track if the ball has collided with a paddle

    def move(self):
        new_x = self.xcor() + self.x_move  # Calculate the new x-coordinate for the ball's movement
        new_y = self.ycor() + self.y_move  # Calculate the new y-coordinate for the ball's movement
        self.goto(new_x, new_y)  # Move the ball to the new coordinates

    def bounce_y(self):
        self.y_move *= -1  # Reverse the y movement to bounce the ball vertically

    def bounce_x(self):
        self.x_move *= -1  # Reverse the x movement to bounce the ball horizontally
        self.move_speed *= 0.9  # Decrease the movement speed by 10% with each bounce

    def reset_position(self):
        self.goto(0, 0)  # Reset the ball's position to the center of the screen
        self.move_speed = 0.1  # Reset the movement speed to its initial value
        self.bounce_x()  # Bounce the ball in a random direction again
