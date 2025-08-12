from turtle import Turtle, Screen, mainloop

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def anti_clockwise():
    turtle.left(10)

def clockwise():
    turtle.right(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()

screen.onkeypress(move_forward,"w")
screen.onkeypress(move_backward,'s')
screen.onkey(anti_clockwise,'a')
screen.onkey(clockwise,'d')
screen.onkey(clear,'c')


screen.exitonclick()