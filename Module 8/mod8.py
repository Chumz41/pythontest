import turtle

def drawSquare(t, sz):
    """Get turtle to draw a square of sz side"""
    for i in range(20):
        t.forward(sz)
        t.left(90)



wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("pink")
drawSquare(alex,50)
wn.exitonclick()

def draw_polygon(sides, length):
    angle = 360 /sides
    for _ in range(sides):
        turtle.forward(length)
        turtle.right(angle)

turtle.speed(0)
turtle.bgcolor("black")
turtle.color("white")

num_polygons = 20
polygon_sides = 8
side_length = 35

for i in range(num_polygons):
    draw_polygon(polygon_sides, side_length)
    turtle.right(360 / num_polygons)

turtle.done()