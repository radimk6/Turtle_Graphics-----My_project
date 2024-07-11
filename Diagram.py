from turtle import Turtle, Screen
import random

colors = ["violet", "yellow", "red", "green", "blue", "pink"]

arrow = Turtle("arrow")
arrow.pensize(2)

for x in range(100):
  arrow.pencolor(colors[x % 6])
  arrow.forward(x)
  arrow.left(60)

my_screen = Screen()
my_screen.exitonclick()