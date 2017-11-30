import turtle

size = input("How large do you want the sides of the star to be? ")

myTurtle = turtle.Turtle()

turns = 5
while(turns > 0 ):
    myTurtle.right(144)
    myTurtle.forward(float(size))
    turns = turns -1


turtle.done()