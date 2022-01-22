import turtle
import random
turtle.penup
rang = input("num")
while True:
    turtle.pendown
    turtle.pensize(6)
    color = ["blue", "red", "green", "yellow", "purple", ]
    for i in range(rang):
        turtle.pencolor(random.choice(color))
        
    break
