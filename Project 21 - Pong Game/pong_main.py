from screen_setup import screen
from paddles import Paddle
from pong_ball import Ball
from scoreboard import Scoreboard
import time

# Create all components needed for the game
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

# Listen for events
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # Update the screen
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        if not ball.collided:
            # Check the direction of the ball's movement
            if ball.x_move > 0 and ball.xcor() + ball.x_move > r_paddle.xcor() - 10:
                # Check if the ball hits the paddles
                if r_paddle.ycor() + 50 > ball.ycor() > r_paddle.ycor() - 50:
                    ball.bounce_x()
                    ball.collided = True
            elif ball.x_move < 0 and ball.xcor() + ball.x_move < l_paddle.xcor() + 10:
                if l_paddle.ycor() + 50 > ball.ycor() > l_paddle.ycor() - 50:
                    ball.bounce_x()
                    ball.collided = True
    else:
        ball.collided = False

    # Detect when paddles miss
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
