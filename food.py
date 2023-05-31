from turtle import Turtle
import random as r

MARGIN: int = 40


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)

    def change_location(self, screen_size):
        max_location = int((screen_size - 2 * MARGIN) / 2)
        random_x = r.randint(-1 * max_location, max_location)
        random_y = r.randint(-1 * max_location, max_location)
        self.goto(random_x, random_y)

    def is_eaten(self, snake):
        if self.distance(snake.head.position()) < 15:
            return True
        else:
            return False
