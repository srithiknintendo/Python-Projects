import turtle 
screen = turtle.Screen()
screen.bgcolor("Black")   
spiral = turtle.Turtle()
spiral.speed(0)
spiral.color("Orange")
spiral.pensize(2)
for i in range(100):
    spiral.forward(i * 5)
    spiral.right(90)


turtle.done()