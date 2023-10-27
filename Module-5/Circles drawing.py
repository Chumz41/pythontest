# My drawing are abstract and are circles randomly drawn
# First we get our turtle name it
# we set it up with drawing diffrent kinds of circles randomly
# so we have to set up with randomness in mind you can see it in our code
# although the randomness can also be manufactured by us to a certain extent
# jose Diaz 27/23

import turtle
import random

wn = turtle.Screen()
artist = turtle.Turtle()

num_circles = int(input("Enter the number of circles:"))

for _ in range(num_circles):
    radius = random.randint(10, 100)
    red = random.random()
    green = random.random()
    blue = random.random()

    artist.penup()
    artist.color(red, green, blue)
    artist.fillcolor(red, green, blue)
    artist.goto(random.randint(-200, 200), random.randint(-200, 200))
    artist.pendown()

    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()

wn.exitonclick()
