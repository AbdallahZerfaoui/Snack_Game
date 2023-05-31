from turtle import Turtle

DISTANCE = 20


class Snake:
    def __init__(self, snake_length=3):
        self.snake_body = [Turtle("square") for _ in range(snake_length)]
        self.create_snake()
        self.head = self.snake_body[-1]

    def create_snake(self):
        # Function to create the initial snake
        for i in range(len(self.snake_body)):
            self.snake_body[i].color("white")
            self.snake_body[i].penup()
            self.snake_body[i].setposition(20 * i, 0)

    def move(self):
        # Function to move the snake
        for i in range(len(self.snake_body) - 1):
            self.snake_body[i].goto(self.snake_body[i + 1].pos())
        self.head.forward(DISTANCE)

    def is_horizontal(self):
        # Function to check if the snake is in a horizontal position
        y_cor_list = []
        for segment in self.snake_body:
            y_cor_list.append(segment.ycor())
        return len(set(y_cor_list)) == 1

    def is_vertical(self):
        # Function to check if the snake is in a vertical position
        x_cor_list = []
        for segment in self.snake_body:
            x_cor_list.append(segment.xcor())
        return len(set(x_cor_list)) == 1

    def up(self):
        # Function to turn the snake upwards
        direction = self.head.heading()
        if direction == 0.0:
            self.head.left(90)
        elif direction == 180.0:
            self.head.right(90)

    def down(self):
        # Function to turn the snake downwards
        direction = self.head.heading()
        if direction == 0.0:
            self.head.right(90)

        elif direction == 180.0:
            self.head.left(90)

    def left(self):
        # Function to turn the snake to the left
        direction = self.head.heading()
        if direction == 90.0:
            self.head.left(90)

        elif direction == 270.0:
            self.head.right(90)

    def right(self):
        # Function to turn the snake to the right
        direction = self.head.heading()
        if direction == 90.0:
            self.head.right(90)

        elif direction == 270.0:
            self.head.left(90)

    def detect_collusion(self):
        distances_list = []
        for block in self.snake_body[:-1]:
            distances_list.append(block.distance(self.head.pos()))

        if abs(self.head.xcor()) >= 280 or abs(self.head.ycor()) >= 260:
            return True
        elif min(distances_list) < 10:
            return True
        else:
            return False

    def extend(self):
        block = Turtle("square")
        block.penup()
        block.color("white")
        block.setposition(self.snake_body[1].pos())
        self.snake_body.insert(0, block)
