from turtle import Turtle, Screen
import random

# Změna barevného módu na RGB
import turtle
turtle.colormode(255)

# Funkce na náhodný výběr barvy pomocí RGB
def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_color = (r, g, b) # Tuple
  return random_color

tommy = Turtle()
tommy.shape("turtle") 

# colors = ["blue", "orange", "green", "red", "pink", "brown", "grey", "yellow"]
move = [0, 90, 180, 270]
speed = 1

for number in range (200):
  # Výběr náhodné barvy
  # tommy.pencolor(random.choice(colors))
  tommy.pencolor(random_color())

  # Zvyšování síly čáry
  if number <= 10:
    tommy.pensize(number)

  # Zvýšení rychlosti
  tommy.speed(speed)
  speed += 1

  # Pohyb a výběr náhodného směru
  tommy.forward(30)
  tommy.right(random.choice(move))

my_screen = Screen()
my_screen.exitonclick()
