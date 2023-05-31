from turtle import Turtle

ALIGNMENT: str = "center"
FONT = ('Courier', 16, 'normal')


class ScoreBoard(Turtle):
    score: int

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
