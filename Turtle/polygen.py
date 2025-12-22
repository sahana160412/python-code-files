import turtle
turtle.Screen().bgcolor('blue')
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
sides=7
sidelength=80
angle=360/sides
for i in range(sides):
    polygon.forward(sidelength)
    polygon.right(angle)
turtle.done()