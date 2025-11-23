import turtle 
screen = turtle.Screen()
screen.bgcolor("orange")   
screen.setup(500,400)

polygone=turtle.Turtle()

numsides = 6
lenght = 70
angle = 360/ numsides

for i in range(numsides):
    polygone.forward(lenght)
    polygone.right(angle)

turtle.done()