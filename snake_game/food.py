from turtle import Turtle,Screen
from random import randint

class Food(Turtle):
    def __init__(self,shape : str = 'circle'):
        super().__init__(shape=shape)
        self.color('red')
        self.penup()
        self.refresh()

    def refresh(self):
        self.setposition(self.generate_coordinate())

    def generate_coordinate(self):
        width = self.screen.window_width()
        height = self.screen.window_height()
        x = randint(-width//2+20, width//2-20)
        y = randint(-height//2+20, height//2-20)
        return (x,y)

        
        
