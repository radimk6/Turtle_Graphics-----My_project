from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)

# Funkce na náhodný výběr barvy pomocí RGB
def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_color = (r, g, b) # Tuple
  return random_color

tommy = Turtle("arrow")
tommy.shape("turtle")
turtle.speed(20)

# == MOJE ŘEŠENÍ ==
# moves = 0

# while moves != 36:
#   tommy.color(random_color())
#   tommy.circle(80)
#   tommy.left(10)
#   moves += 1

# == ŘEŠENÍ DAVID ŠETEK ==
# for number in range(36):
#   tommy.color(random_color())
#   tommy.circle(80)
#   tommy.left(10)

def spirograph(gap):
  for number in range(int(360/gap)):
   tommy.color(random_color())
   tommy.circle(80)
   tommy.left(gap)

spirograph(10)

my_screen = Screen()
my_screen.exitonclick()