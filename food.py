from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_len=0.75, stretch_wid=0.75, outline=None)
        self.speed("fastest")
        self.penup()
        self.appear()

    def appear(self):
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)