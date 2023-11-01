import turtle
import random


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_1 = random.randint(-260, 260)
        random_2 = random.randint(-260, 260)
        self.goto(x=random_1, y=random_2)
