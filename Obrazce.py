from turtle import Turtle, Screen
import random

line_color = ["blue", "orange", "green", "red", "pink", "brown", "grey", "yellow"]

tommy = Turtle()
tommy.shape("turtle")
tommy.pensize(2)

# == MOJE ŘEŠENÍ ==
x = 360
y = 2

for __ in range(6):
  y += 1
  tommy.pencolor(random.choice(line_color))
  for _ in range(y):
    i = x / y
    tommy.forward(100)
    tommy.right(i)

# == ŘEŠENÍ DAVID ŠETEK ==
# moves = 3

# while moves != 9:
#   random_color = random.choice(line_color)
#   tommy.pencolor(random_color)
#   for _ in range(moves):
#     tommy.forward(100)
#     tommy.right(360/moves)
#   moves += 1

my_screen = Screen()
my_screen.exitonclick()