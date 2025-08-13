from turtle import Screen
from SnakeBody import Snake

def game_loop():
    snake.move_forward()
    screen.ontimer(game_loop, 150) 

screen = Screen()
screen.tracer(0)
snake = Snake()

screen.listen()
screen.onkey(snake.turn_left, 'a')
screen.onkey(snake.turn_up, 'w')
screen.onkey(snake.turn_right, 'd')
screen.onkey(snake.turn_down, 's')


if __name__ =="__main__":
    game_loop() 
    screen.mainloop()