from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class as the base class for Food
        self.shape("circle")  # Set the shape of the food to a circle
        self.color("red")  # Set the color of the food to red
        self.penup()  # Lift the pen to avoid drawing lines while moving
        self.speed(0)  # Set the speed of the food's animation to the fastest
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)  # Stretch the size of the food
        random_x = random.randint(-280, 280)  # Generate a random x-coordinate within the game window
        random_y = random.randint(-280, 280)  # Generate a random y-coordinate within the game window
        self.goto(random_x, random_y)  # Move the food to the randomly generated coordinates
        self.refresh()  # Call the refresh method to update the food's position

    def refresh(self):
        """Move the food to a random position."""
        random_x = random.randint(-280, 280)  # Generate a new random x-coordinate
        random_y = random.randint(-280, 280)  # Generate a new random y-coordinate
        self.goto(random_x, random_y)  # Move the food to the new random coordinates
