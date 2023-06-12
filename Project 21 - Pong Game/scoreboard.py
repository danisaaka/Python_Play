from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")  # Set the color of the scoreboard text to white
        self.penup()
        self.hideturtle()  # Hide the turtle icon
        self.l_score = 0  # Initialize the left player's score to 0
        self.r_score = 0  # Initialize the right player's score to 0

    def update_scoreboard(self):
        self.clear()  # Clear the previous score display
        self.goto(-100, 200)  # Position the turtle to display the left player's score
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))  # Write the left player's score
        self.goto(100, 200)  # Position the turtle to display the right player's score
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))  # Write the right player's score

    def l_point(self):
        self.l_score += 1  # Increment the left player's score by 1
        self.update_scoreboard()  # Update the scoreboard display

    def r_point(self):
        self.r_score += 1  # Increment the right player's score by 1
        self.update_scoreboard()  # Update the scoreboard display
