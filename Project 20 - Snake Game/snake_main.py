from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn-off screen updates

# Create instances of the Snake, Food, and Scoreboard classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for key events to control the snake's movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # Update the screen
    time.sleep(0.1)  # Pause the game for a short duration

    snake.move()  # Move the snake

    # Detect collision with food
    if snake.head.distance(food) < 18:
        food.refresh()  # Move the food to a random position
        scoreboard.increment_score()  # Increase the score
        snake.grow()  # Make the snake grow

    # Detect collision with wall
    if (
        snake.head.xcor() > 300
        or snake.head.xcor() < -300
        or snake.head.ycor() > 300
        or snake.head.ycor() < -300
    ):
        game_is_on = False  # End the game
        scoreboard.game_over()  # Display the "Game Over" message

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display the "Game Over" message

screen.exitonclick()  # Close the window when clicked
