from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.color("DarkSeaGreen")
        self.speed(0)
        self.refresh_food()

    def refresh_food(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x=x, y=y)
