import turtle

STARTING_SNAKE = 3
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.turtles = []
        self.creating_snake()
        self.head = self.turtles[0]

    def creating_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake = turtle.Turtle()
        snake.color('white')
        snake.shape('square')
        snake.penup()
        snake.goto(position)
        self.turtles.append(snake)

    def extend(self):
        self.add_segment(self.turtles[-1].position())

    def snake_forward(self):
        for j in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[j - 1].xcor()
            new_y = self.turtles[j - 1].ycor()
            self.turtles[j].goto(new_x, new_y)
        self.head.fd(SPEED)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
