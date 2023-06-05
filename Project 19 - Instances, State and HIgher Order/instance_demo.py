from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


screen.listen()
screen.onkey(fun=move_forward, key="space")
screen.exitonclick()
