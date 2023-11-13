# Jose Diaz 11/12/23
# Work of what we have
# we create a new parameter so we can have it draw a square x number of times

# Q5





import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

def drawmoreSquares(t, num_squares, initial_size, size_increment):
# Its important to have the penup and down if not it does appear like in the picture
    for _ in range(num_squares):
        drawSquare(t, initial_size)
        t.penup()
        t.backward(size_increment / 2)
        t.right(90)
        t.forward(size_increment / 2)
        t.left(90)
        t.pendown()
        initial_size += size_increment

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")
# we set our values so it draws the ammount of squares we want with size increments
drawmoreSquares(alex, 4, 20, 20)

wn.exitonclick()
