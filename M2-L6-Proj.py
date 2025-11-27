import turtle 
screen = turtle.Screen()
screen.bgcolor("red")   
screen.setup(500,400)

polygone=turtle.Turtle()

numsides = 4
lenght = 50
angle = 360/ numsides

for i in range(numsides):
    polygone.forward(lenght)
    polygone.right(angle)

turtle.done()