from turtle import Turtle

START_POSITIONS = [(0, 0), (-10, 0), (-20, 0)]
SPEED = 10
MOVE_DISTANCE = 7
SIZE = 0.5


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in START_POSITIONS:
            self.add_segment(_)

    def add_segment(self, positions):
        new_body = Turtle("square")
        new_body.color("white")
        new_body.turtlesize(SIZE)
        new_body.penup()
        new_body.speed(SPEED)
        new_body.goto(positions)
        self.segments.append(new_body)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for body in range(len(self.segments) - 1, 0, -1):
            x = self.segments[body - 1].xcor()
            y = self.segments[body - 1].ycor()
            self.segments[body].goto(x, y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def game_over(self):
        self.color("white")
        self.hideturtle()
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]