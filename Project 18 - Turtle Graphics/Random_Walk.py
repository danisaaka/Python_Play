import random
import turtle

from Turtles import timmy, tom, harry, screen

turtle.colormode(255)


def generate_random_colour():
    """
    Function to generate a random RGB color.
    :return: A tuple representing the RGB values of the generated color.
    """
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return red, green, blue


def move_turtle(turtle, direction, step_distance):
    """
    Function to move a turtle in the specified direction by the given step distance.
    It also changes the pen color of the turtle to a random color using generate_random_colour() function.
    :param turtle: The turtle object to be moved.
    :param direction: The direction in which the turtle should move ("up", "down", "left", "right").
    :param step_distance: The distance by which the turtle should move in each step.
    """
    if direction == "up":
        turtle.setheading(90)  # Point turtle up
    elif direction == "down":
        turtle.setheading(270)  # Point turtle down
    elif direction == "left":
        turtle.setheading(180)  # Point turtle left
    else:
        turtle.setheading(0)  # Point turtle right

    turtle.forward(step_distance)
    turtle.pencolor(generate_random_colour())


# Define the possible directions
directions = ["up", "down", "left", "right"]
num_steps = 500
timmy_step_distance = 25
tom_step_distance = 25

# Perform the random walk for all turtles
for _ in range(num_steps):
    timmy_direction = random.choice(directions)
    tom_direction = random.choice(directions)

    # Move Timmy
    move_turtle(timmy, timmy_direction, timmy_step_distance)
    # Move Tom
    move_turtle(tom, tom_direction, tom_step_distance)
    # Move Harry
    move_turtle(harry, random.choice(directions), timmy_step_distance)

screen.exitonclick()
