from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)  # Position near top
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over_message(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
