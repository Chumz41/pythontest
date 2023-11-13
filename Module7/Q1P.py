# Jose Diaz 11/12/23
# use the import function to use it in our parameters below to get the area
# Q1



import math

def areaofCircle(r):
    if r < 0:
        return "cannot calculate radius if integer is negative."
    else:
        area = math.pi * r**2
        return area

# test it if it works using an integer and a negative one

radius = -5
result = areaofCircle(radius)
print(f"The area of a circle with radius {radius} is: {result}")
