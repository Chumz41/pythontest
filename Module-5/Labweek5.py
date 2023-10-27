# jose Diaz 27/23
# we import our turtle and set up its variables and create a polygon with it


import turtle

wn = turtle.Screen()
goob = turtle.Turtle()

sides = int(input("Number of sides in polygon?"))
length = int(input("Length of the sides in polygon?"))
colorname = input("Color of polygon?")
fcolor = input("Fill color of polygon?")

goob.color(colorname)
goob.fillcolor(fcolor)
goob.begin_fill()

for i in range(sides):
   goob.forward(length)
   goob.left(360 / sides)

goob.end_fill()
wn.exitonclick()
