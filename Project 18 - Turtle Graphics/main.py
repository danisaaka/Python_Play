import turtle
import random

from Turtles import screen, timmy

turtle.colormode(255)


def random_colour():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    colour = (red, green, blue)
    return colour


def draw_spirograph(turtle_object, size_of_gap, radius):
    """ Draws a spirograph
    :param turtle_object: turtle object
    :param size_of_gap: The size of the gap between the circles
    :param radius: The radius of the circles
    :return: None
    """
    for _ in range(int(360 / size_of_gap)):
        turtle_object.color(random_colour())
        turtle_object.circle(radius)
        turtle_object.setheading(timmy.heading() + size_of_gap)


print("You are about to draw a spirograph.")
bigger_circle = int(input("Key in the radius of the bigger circle.\n"))
bigger_gap = int(input("Key in the gap of the bigger circle.\n"))
smaller_circle = int(input("Key in the radius of the smaller circle.\n"))
smaller_gap = int(input("Key in the gap of the smaller circle.\n"))

draw_spirograph(timmy, bigger_gap, bigger_circle)
draw_spirograph(timmy, smaller_gap, smaller_circle)

screen.exitonclick()
