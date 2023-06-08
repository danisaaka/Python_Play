from turtle import Turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_MOVEMENT = 20


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.paddle = Turtle()
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        # Set the turtle position
        self.x = x
        self.y = y
        # Set turtle shape to "square" and change color
        self.paddle.shape("square")
        self.paddle.color("white")
        # Set turtle size to fixed width and height
        self.paddle.shapesize(stretch_wid=self.height/20, stretch_len=self.width/20)
        # Move the paddle to the specified position
        self.paddle.penup()
        self.paddle.goto(self.x, self.y)

    def move_paddle(self, direction):
        if direction == "up":
            new_y = self.paddle.ycor() + PADDLE_MOVEMENT
        elif direction == "down":
            new_y = self.paddle.ycor() - PADDLE_MOVEMENT
        else:
            return
        self.paddle.sety(new_y)
