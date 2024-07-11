from turtle import Turtle, Screen

tommy = Turtle()
tommy.shape("turtle")

"""
Vytvoření čtverce v příkazech za sebou
tommy.forward(150)
tommy.right(90)
tommy.forward(150)
tommy.right(90)
tommy.forward(150)
tommy.right(90)
tommy.forward(150)
"""

# Vytvoření čtverce pomocí cyklu
for _ in range(4):
  tommy.forward(150)
  tommy.left(90)

my_screen = Screen()
my_screen.exitonclick()