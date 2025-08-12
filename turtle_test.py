import turtle as t
from random import random,choice,randint

turtle = t.Turtle()
turtle.pensize(8)
t.colormode(255)

def color_gen() -> tuple:
    r = randint(1,255)
    g = randint(1,255)
    b = randint(1,255)
    return (r,g,b)

def draw_shape(turtle : t.Turtle, sides : int, color : str):
    turtle.fillcolor(color)
    angle = 360 / sides
    turtle.color(color_gen())
    for _ in range(sides):
        turtle.forward(100)
        turtle.right(angle)
    turtle.clear()
    turtle.home()

if __name__ == "__main__":
    for side in range(3,100):
        color = choice(['red','blue','yellow'])
        draw_shape(turtle,side,color)
    t.mainloop()


