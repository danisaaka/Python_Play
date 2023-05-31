from turtle import Turtle, Screen
import random

# List of colors
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]

# Initialize the screen
screen = Screen()
screen.setup(width=750, height=600)
screen.bgcolor("black")

# Initialize the first turtle (Timmy)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(3)

# Initialize the second turtle (Tom)
tom = Turtle()
tom.shape("turtle")
tom.color("blue")
tom.pensize(2)


def draw_shape(num_sides):
    # Calculate the angle for each side of the shape
    angle = 360 / num_sides

    # Draw the shape using both Timmy and Tom
    for _ in range(num_sides):
        timmy.forward(80)
        tom.forward(80)
        timmy.right(angle)
        tom.left(angle)


# Loop through shapes from triangle to do-decagon
for shape_side_n in range(3, 20):
    # Set a random color for Timmy and Tom from the list of colors
    timmy.color(random.choice(colours))
    tom.color(random.choice(colours))

    # Draw the shape with the current number of sides
    draw_shape(shape_side_n)

# Exit the program when the screen is clicked
screen.exitonclick()
