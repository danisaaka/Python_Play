from screen_setup import screen
from paddles import Paddle
from pong_ball import Ball
import time

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

# Listen for events
screen.listen()
screen.onkey(lambda: r_paddle.move_paddle("up"), "Up")
screen.onkey(lambda: l_paddle.move_paddle("up"), "w")
screen.onkey(lambda: r_paddle.move_paddle("down"), "Down")
screen.onkey(lambda: l_paddle.move_paddle("down"), "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()  # Update the screen
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

screen.exitonclick()
