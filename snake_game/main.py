from turtle import Screen,Turtle
from SnakeBody import Snake
from scoreboard import ScoreBoard
from food import Food

TIMER = 120

GAME_IS_ON = True
cnt = 0

screen = Screen()
screen.tracer(0)


snake = Snake()
food = Food()


scoreboard = ScoreBoard()

def game_loop():
    global GAME_IS_ON
    if snake.collision():
        GAME_IS_ON = False
        scoreboard.game_over_message()
        return
    if snake.collision_with_food(food):
        scoreboard.score += 1
        scoreboard.update_score()
        food.refresh()
        snake.increase_size()
    snake.move_forward()
    screen.ontimer(game_loop, TIMER)

screen.listen()
screen.onkey(snake.turn_left, 'a')
screen.onkey(snake.turn_up, 'w')
screen.onkey(snake.turn_right, 'd')
screen.onkey(snake.turn_down, 's')

if __name__ =="__main__":
    game_loop() 
    screen.mainloop()