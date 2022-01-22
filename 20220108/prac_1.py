import turtle
import random
turtle.penup

while True:
    turtle.pendown
    turtle.pensize(6)
    color = ["blue", "red", "green", "yellow", "purple", ]
    for i in range(5):
        turtle.pencolor(random.choice(color))
        turtle.forward(100)
        turtle.right(144)
    break
