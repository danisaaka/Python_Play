from turtle import Turtle, Screen
import random

# Set a flag to control the race
is_race_on = False

# Set up the screen for the race
screen = Screen()
screen.setup(width=500, height=400)

# Prompt the user to bet on a turtle
user_bet = screen.textinput(title="Place Your Bet",
                            prompt="Which turtle do you think will win the race? Enter a color from the list\n"
                                   "('red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black'), "
                                   "or type 'quit' to exit: ")

# Define the colors for the turtles
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black']

# Set the initial positions for the first turtle
x_axis = -230
y_axis = -150

# Create a list to store all the turtles
all_turtles = []

# Create turtles for each color and set their initial properties
for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=x_axis, y=y_axis)
    y_axis += 50
    all_turtles.append(new_turtle)

# Check if the user has made a valid bet or wants to quit
while user_bet.lower() not in [color.lower() for color in colors] and user_bet.lower() != "quit":
    user_bet = screen.textinput(title="Invalid Input",
                                prompt="Invalid color. Please enter a color from the list "
                                       "('red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black'), "
                                       "or type 'quit' to exit: ")

# Check if the user wants to quit
if user_bet.lower() == "quit":
    screen.bye()

# Start the race
if user_bet:
    is_race_on = True

# Create a turtle for displaying the winner
winner_turtle = Turtle()
winner_turtle.hideturtle()
winner_turtle.penup()
winner_turtle.goto(0, -100)

while is_race_on:
    # Move each turtle forward by a random distance
    for turtle in all_turtles:
        # Check if a turtle has reached the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            # Check if the user's bet matches the winning turtle's color
            if winning_color.lower() == user_bet.lower():
                winner_turtle.write(f"You have won!! The {winning_color} turtle is the winner!",
                                    align="center", font=("Arial", 16, "bold"))
            else:
                winner_turtle.write(f"You lost!! The {winning_color} turtle is the winner!",
                                    align="center", font=("Arial", 16, "bold"))

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Close the screen when clicked
screen.exitonclick()
# In this updated code, a new turtle object named winner_turtle is created to display the winning message.
# The write() method is used to display the message on the screen. The position of the winner_turtle is set to (0,
# -100) to center it at the bottom of the screen. The align parameter is set to "center" to align the text in the
# middle, and the font parameter used to customize the font properties.
#
# Now, when the race finishes, the winning message will be displayed on the screen using the winner_turtle,
# rather than printing it to the console.
