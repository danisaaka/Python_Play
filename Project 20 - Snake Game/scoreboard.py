from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle class as the base class for Scoreboard
        self.score = 0  # Initial score value
        self.color("white")  # Set the color of the scoreboard to white
        self.penup()  # Lift the pen to avoid drawing lines while moving
        self.goto(0, 270)  # Set the initial position of the scoreboard
        self.hideturtle()  # Hide the turtle icon
        self.update_score()  # Call the update_score method to display the initial score

    def update_score(self):
        """Update and display the score on the scoreboard."""
        self.clear()  # Clear the previous score
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # Write the new score on the scoreboard

    def increment_score(self):
        """Increment the score by 1 and update the scoreboard."""
        self.score += 1  # Increment the score by 1
        self.update_score()  # Call the update_score method to display the updated score

    def game_over(self):
        """Display the 'Game Over' message on the scoreboard."""
        self.goto(0, 0)  # Move to the center of the screen
        self.write("Game Over", align=ALIGNMENT, font=FONT)  # Write 'Game Over' on the scoreboard
