from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time as t

# **** INPUTS **** #
screen_size = 600
screen_color = "black"

# **** Initialization **** #
game_is_on = True

# **** Objects creation **** #
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# **** Screen setting **** #
screen = Screen()
screen.setup(width=screen_size, height=screen_size)
screen.title("Snake Game")
screen.bgcolor(screen_color)
screen.tracer(0)
screen.listen()
# Snake control
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# Snake movement
food.change_location(screen_size)

while game_is_on:
    snake.move()
    if food.is_eaten(snake):
        food.change_location(screen_size)
        scoreboard.increase_score()
        snake.extend()
        # print(len(snake.snake_body))

    if snake.detect_collusion():
        game_is_on = False
        scoreboard.game_over()

    screen.update()
    t.sleep(0.2)

screen.exitonclick()
