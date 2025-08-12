from turtle import Turtle
class Player(Turtle):
    def __init__(self,color) -> None:
        super().__init__()
        self.color(color)
        self.shape("turtle")