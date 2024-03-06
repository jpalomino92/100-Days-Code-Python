from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0),(-20, 0),(-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        snake_body_part = Turtle(shape="square")
        snake_body_part.color("white")
        snake_body_part.penup()
        snake_body_part.goto(position)
        self.body.append(snake_body_part)

    def extend(self):
        self.add_segment(self.body[-1].position())

    def reset(self):
        for b in self.body:
            b.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def move(self):
        for s in range(len(self.body) - 1, 0, -1):
            new_x = self.body[s - 1].xcor()
            new_y = self.body[s - 1].ycor()
            self.body[s].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


