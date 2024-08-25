import turtle
import math
import random

itemNum = 0
maxItem = 10

sizeNum = 0
sizes = [5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80, 90, 100]

colorNum = 0
colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan",
    "magenta", "brown", "black", "white", "navy", "turquoise", "violet",
    "gold", "silver", "indigo", "maroon", "lime"
]

turtle.setup(800, 600)
turtle.title("Turtle Drawing pad")
turtle.hideturtle()
turtle.speed(0)
turtle.up()


def drawItem(x, y):
  global itemNum
  shapes = [
      circle, square, triangle, star, hexagon, spiral, heart, arrow,
      custom_turtle, random_shape
  ]
  shapes[itemNum](x, y)


def circle(x, y):
  turtle.begin_fill()
  turtle.goto(x, y - sizes[sizeNum])
  turtle.circle(sizes[sizeNum])
  turtle.end_fill()


def square(x, y):
  turtle.begin_fill()
  turtle.goto(x - (sizes[sizeNum] / 2), y - (sizes[sizeNum] / 2))
  turtle.setheading(0)
  for _ in range(4):
    turtle.forward(sizes[sizeNum])
    turtle.left(90)
  turtle.end_fill()


def triangle(x, y):
  turtle.goto(x - (sizes[sizeNum] / 2),
              y - ((sizes[sizeNum] * math.sqrt(3)) / 6))
  turtle.setheading(0)
  turtle.begin_fill()
  for _ in range(3):
    turtle.forward(sizes[sizeNum])
    turtle.left(120)
  turtle.end_fill()


def star(x, y):
  turtle.goto(x, y)
  turtle.setheading(0)
  turtle.begin_fill()
  for _ in range(5):
    turtle.forward(sizes[sizeNum])
    turtle.right(144)
  turtle.end_fill()


def hexagon(x, y):
  turtle.goto(x, y)
  turtle.setheading(0)
  turtle.begin_fill()
  for _ in range(6):
    turtle.forward(sizes[sizeNum] / 2)
    turtle.left(60)
  turtle.end_fill()


def spiral(x, y):
  turtle.goto(x, y)
  turtle.setheading(0)
  for i in range(36):
    turtle.forward(i * 2)
    turtle.right(30)


def heart(x, y):
  turtle.goto(x, y)
  turtle.setheading(0)
  turtle.begin_fill()
  turtle.left(140)
  turtle.forward(sizes[sizeNum])
  for _ in range(200):
    turtle.right(1)
    turtle.forward(sizes[sizeNum] * 0.01)
  turtle.left(120)
  for _ in range(200):
    turtle.right(1)
    turtle.forward(sizes[sizeNum] * 0.01)
  turtle.forward(sizes[sizeNum])
  turtle.end_fill()


def arrow(x, y):
  turtle.goto(x, y)
  turtle.setheading(0)
  turtle.begin_fill()
  turtle.forward(sizes[sizeNum] * 2)
  turtle.left(120)
  turtle.forward(sizes[sizeNum])
  turtle.left(120)
  turtle.forward(sizes[sizeNum])
  turtle.left(120)
  turtle.forward(sizes[sizeNum] * 2)
  turtle.left(150)
  turtle.forward(sizes[sizeNum] * 1.5)
  turtle.end_fill()


def custom_turtle(x, y):
  turtle.goto(x, y)
  turtle.setheading(0)
  turtle.begin_fill()
  turtle.circle(sizes[sizeNum] / 2, 180)
  turtle.circle(sizes[sizeNum] / 4, 180)
  turtle.left(180)
  turtle.circle(-sizes[sizeNum] / 4, 180)
  turtle.circle(-sizes[sizeNum] / 2, 180)
  turtle.end_fill()


def random_shape(x, y):
  turtle.goto(x, y)
  turtle.setheading(random.randint(0, 360))
  turtle.begin_fill()
  for _ in range(random.randint(3, 8)):
    turtle.forward(random.randint(20, 100))
    turtle.left(random.randint(30, 150))
  turtle.end_fill()


def switchColor(x, y):
  global colorNum
  colorNum = (colorNum + 1) % len(colors)
  turtle.color(colors[colorNum])


def switchSize(x, y):
  global sizeNum
  sizeNum = (sizeNum + 1) % len(sizes)


def switchShape(x, y):
  global itemNum
  itemNum = (itemNum + 1) % maxItem


def toggleFill(x, y):
  if turtle.filling():
    turtle.end_fill()
  else:
    turtle.begin_fill()


def clearScreen(x, y):
  turtle.clear()


def randomColor(x, y):
  turtle.color(random.choice(colors))


turtle.onscreenclick(drawItem, 1)
turtle.onscreenclick(switchSize, 2)
turtle.onscreenclick(switchShape, 3)

turtle.onkey(lambda: switchSize(0, 0), "s")
turtle.onkey(lambda: switchShape(0, 0), "d")
turtle.onkey(lambda: switchColor(0, 0), "c")
turtle.onkey(lambda: toggleFill(0, 0), "f")
turtle.onkey(lambda: clearScreen(0, 0), "x")
turtle.onkey(lambda: randomColor(0, 0), "r")

turtle.goto(-380, 270)
turtle.write(
    "Left click: Draw | Right click: Change size | Middle click: Change shape",
    align="left",
    font=("Arial", 12, "normal"))
turtle.goto(-380, 250)
turtle.write(
    "'s': Change size  'd': Change shape  'c': Change color  'f': Toggle fill  'x': Clear  'r': Random color",
    align="left",
    font=("Arial", 12, "normal"))

turtle.listen()
turtle.mainloop()
