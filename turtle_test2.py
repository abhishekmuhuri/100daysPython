import turtle as t

turtle = t.Turtle()
turtle.speed(0)
t.colormode(255)
turtle.pensize(2)

for i in range(40):
    turtle.left(10)
    turtle.circle(100)

print(f'Done')
t.done()