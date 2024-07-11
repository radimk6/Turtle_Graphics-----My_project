from turtle import Turtle, Screen

# == Řešení pomocí 2 šipek ==
# arrow = Turtle("arrow")
# arrow.pensize(2)
# arrow.pencolor("green")
# dart = Turtle("arrow")
# dart.pensize(2)
# dart.pencolor("red")

# circle = 20

# dart.circle(circle)

# for _ in range(10):
#   circle += 10
#   arrow.circle(circle)

# == Řešení pomocí jedné šipky ==
# arrow = Turtle("arrow")
# arrow.pensize(2)

# circle = 20

# for _ in range(10):
#   if circle == 20:
#     arrow.pencolor("red")
#   else:
#     arrow.pencolor("green")
#   arrow.circle(circle)
#   circle += 10

# == Řešení David Šetek ==
arrow = Turtle("arrow")
arrow1 = Turtle("arrow")
arrow.pencolor("red")
arrow1.pencolor("green")
arrow.pensize(2)
arrow1.pensize(2)

arrow.circle(20)

for i in range(30, 100, 10):
  arrow1.circle(i)

screen = Screen()
screen.exitonclick()