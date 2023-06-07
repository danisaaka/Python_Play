from turtle import Turtle

# Initial positions of the snake segments and other constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []  # List to store the turtle segments
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # Head of the snake

    def create_snake(self):
        """Create the initial snake with segments."""
        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """Move the snake forward."""
        for segment_number in range(len(self.segments) - 1, 0, -1):
            # Move each segment to the position of the previous segment
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)  # Move the head segment

    def change_direction(self, heading):
        """Change the direction of the snake's movement."""
        self.segments[0].setheading(heading)  # Set the heading of the head segment
        for segment in self.segments:
            segment.setheading(heading)  # Set the heading of all segments
            segment.forward(MOVE_DISTANCE)  # Move each segment

    def up(self):
        """Change the snake's direction to up if it's not already moving down."""
        if self.segments[0].heading() != DOWN:
            self.change_direction(UP)

    def down(self):
        """Change the snake's direction to down if it's not already moving up."""
        if self.segments[0].heading() != UP:
            self.change_direction(DOWN)

    def left(self):
        """Change the snake's direction to left if it's not already moving right."""
        if self.segments[0].heading() != RIGHT:
            self.change_direction(LEFT)

    def right(self):
        """Change the snake's direction to right if it's not already moving left."""
        if self.segments[0].heading() != LEFT:
            self.change_direction(RIGHT)

    def grow(self):
        """Add a new segment to the snake."""
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_segment)
