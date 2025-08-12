from typing import List,Union
from random import randint
from Player import Player

INITIAL_DIS_Y = 30
TOTAL_PLAYERS = 4
WINNING_DIS = 300
WINNER_FOUND = False

from turtle import Turtle,Screen


def move_all_players(all_players : List[Player], betting_color : str) -> None:
    for player in all_players:
        player.forward(randint(5,8))
        x,_ = player.pos()
        global WINNER_FOUND
        if x>=WINNING_DIS:
            print(f"We have a winner!!! {player.color()[0]}")
            WINNER_FOUND = True
            if betting_color.strip().lower() == player.color()[0]:
                print(f"You have won the bet!!")
            else: print("You have lost the bet")


screen = Screen()
screen.setup(900,600)

all_players = []

all_colors = ["red","blue","yellow","pink"]

last_y = 0

for color in all_colors:
    player = Player(color)
    all_players.append(player)
    player.teleport(y=last_y+INITIAL_DIS_Y)
    _, last_y = player.pos()

betting_color = ""
while True:
    input_color = screen.textinput("BET ON! ", "Enter the color of the turtle you wanna bet on!")
    if input_color is None:
        exit()
    elif input_color in all_colors:
        betting_color = input_color
        break

while not WINNER_FOUND and input_color is not None:
    move_all_players(all_players,betting_color)


screen.mainloop()


