from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def reset_timmy():
    timmy.reset()
    timmy.penup()
    timmy.home()
    timmy.pendown()


def move_forward():
    timmy.forward(25)


def move_backward():
    timmy.backward(25)


def move_left():
    timmy.left(15)


def move_right():
    timmy.right(15)


screen.listen()

screen.onkey(fun=reset_timmy, key="c")
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")

screen.exitonclick()
