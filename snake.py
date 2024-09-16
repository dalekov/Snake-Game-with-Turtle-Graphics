from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()

    # A new segment is added to the body of the snake:
    def add_segment(self, position):
        segment = Turtle("square")
        segment.color("green")
        segment.speed("fastest")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    # We create the initial body of the snake - 3 segments
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Extend the snake when food is consumed - we simply add a new segment on the position of the last one.
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Function to move the snake - we loop through each segment and tell it to go to the coords of the one before it,
    # thus creating a snake-like movement. The head of the snake advances by 20px.
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)

        self.segments[0].forward(20)


    # Functions to control the snake with the keyboard - if the snake is facing down, it can't go up and so on.
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

