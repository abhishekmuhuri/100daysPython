from turtle import Turtle,_Screen
from typing import List

class Snake:
    def __init__(self) -> None:
        last_x = 0
        self.all_bodies: List[Turtle] = []
        self.__CHANGE_DIRECTION_STATE: bool = True
        for _ in range(3):
            body = Turtle("square")
            body.penup()
            body.teleport(-last_x,0)
            last_x-=20
            self.all_bodies.append(body)
        self.head = self.all_bodies[-1]
        self.screen = self.head.screen

    def get_screen(self):
        return self.head.screen

    def get_head(self) -> Turtle:
        return self.all_bodies[-1]

    def move_forward(self) -> None:
        all_pos = []
        self.__CHANGE_DIRECTION_STATE = False
        for body in self.all_bodies:
            all_pos.append(body.pos())
        for i in range(len(all_pos)-2,-1,-1):
            curr_body = self.all_bodies[i]
            curr_body.goto(all_pos[i+1])
        self.head.forward(20)
        self.screen.update()
        self.__CHANGE_DIRECTION_STATE = True

    @property
    def CHANGE_DIRECTION_STATE(self) -> bool:
        return self.__CHANGE_DIRECTION_STATE
    
    def can_change_direction(self) -> bool:
        return self.CHANGE_DIRECTION_STATE == True

    def facing_upward(self):
        return self.head.heading() == 90
    def facing_downward(self):
        return self.head.heading() == 270
    
    def facing_left(self):
        return self.head.heading() == 180
    
    def facing_right(self):
        return self.head.heading() == 0

    def turn_left(self):
        if self.can_change_direction() and not self.facing_right():
            self.head.setheading(180)
    def turn_right(self):
        if self.can_change_direction() and not self.facing_left():
            self.head.setheading(0)
    def turn_down(self):
        if self.can_change_direction() and not self.facing_upward():
            self.head.setheading(270)
    def turn_up(self):
        if self.can_change_direction() and not self.facing_downward():
            self.head.setheading(90)