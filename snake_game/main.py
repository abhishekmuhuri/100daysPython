from turtle import Screen, Turtle
from SnakeBody import Snake
from scoreboard import ScoreBoard
from food import Food


class SnakeGame:
    """Snake game controller that manages game state and loop."""

    TIMER = 120

    def __init__(self):
        """Initialize game components and state."""
        self.screen = Screen()
        self.screen.tracer(0)
        self.snake = Snake()
        self.food = Food()
        self.scoreboard = ScoreBoard()
        self.game_is_on = True

    def setup_controls(self):
        """Configure keyboard controls for the game."""
        self.screen.listen()
        self.screen.onkey(self.snake.turn_left, 'a')
        self.screen.onkey(self.snake.turn_up, 'w')
        self.screen.onkey(self.snake.turn_right, 'd')
        self.screen.onkey(self.snake.turn_down, 's')
        self.screen.onkey(self.reset, 'space')

    def reset(self):
        """Reset the game to initial state."""
        if not self.game_is_on:
            self.screen.clearscreen()
            self.screen.resetscreen()
            self.screen.tracer(0)
            self.snake = Snake()
            self.food = Food()
            self.scoreboard = ScoreBoard()
            self.game_is_on = True
            self.setup_controls()
            self.game_loop()
            self.screen.mainloop()

    def game_loop(self):
        """Main game loop that handles game logic and updates."""
        if self.snake.collision():
            self.game_is_on = False
            self.scoreboard.game_over_message()
            return

        if self.snake.collision_with_food(self.food):
            self.scoreboard.score += 1
            self.scoreboard.update_score()
            self.food.refresh()
            self.snake.increase_size()

        self.snake.move_forward()
        self.screen.ontimer(self.game_loop, self.TIMER)

    def run(self):
        """Start and run the game."""
        self.setup_controls()
        self.game_loop()
        self.screen.mainloop()


if __name__ == "__main__":
    game = SnakeGame()
    game.run()
