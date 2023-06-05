from turtle import Turtle, Screen

# Initialize the screen
screen = Screen()
screen.setup(width=750, height=600)
screen.bgcolor("black")
# Initialize the first turtle (Timmy)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.pensize(2)
timmy.speed(0)

# Initialize the second turtle (Tom)
tom = Turtle()
tom.shape("turtle")
tom.color("blue")
tom.pensize(10)
tom.speed(0)

# Initialize the third turtle (Harry)
harry = Turtle()
harry.shape("turtle")
harry.color("green")
harry.pensize(10)
harry.speed(0)