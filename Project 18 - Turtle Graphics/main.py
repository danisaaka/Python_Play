from turtle import Turtle, Screen

# Create a Turtle object
turtle = Turtle()

# Set the pen color and thickness
turtle.pencolor("black")
turtle.pensize(2)

# Set the pen to draw in dotted style
turtle.pen(pendown=False, pencolor="black", pensize=2)

# Move the turtle to the starting position
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()

# Draw the dotted square
for _ in range(50):
    turtle.forward(50)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    turtle.right(90)

# Create a Screen object to keep the turtle graphics window open
screen = Screen()
screen.mainloop()
turtle.done()
