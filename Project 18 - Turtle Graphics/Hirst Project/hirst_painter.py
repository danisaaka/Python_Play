import random
import turtle

# Import the color_list from the hirst_main module
from hirst_main import color_list

# Set up the Turtle window
window = turtle.Screen()
window.bgcolor("black")

# Set the color mode to 255 (RGB color values range from 0 to 255)
turtle.colormode(255)

# Create a new turtle object
artist = turtle.Turtle()
artist.speed(0)  # Set the drawing speed (0 is the fastest)

# Define the size and spacing of each dot
dot_size = 20
dot_spacing = 50

# Prompt the user to enter the number of rows and columns
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# You can check for how this loop works in the  txt file included in the directory
# Iterate over each row
for row in range(rows):
    # Iterate over each column
    for column in range(columns):
        # Calculate the position of the dot
        x = column * dot_spacing - (dot_spacing * (columns - 1)) / 2
        y = row * dot_spacing - (dot_spacing * (rows - 1)) / 2

        # Move the artist to the appropriate position
        artist.penup()
        artist.goto(x, y)
        artist.pendown()

        # Select a random color for the dot
        color = random.choice(color_list)
        artist.color(color)

        # Draw a dot
        artist.dot(dot_size)

# Hide the turtle
artist.hideturtle()

# Keep the turtle window open until it is clicked
window.exitonclick()

