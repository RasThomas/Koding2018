import turtle
import math

myTurtle = turtle.Turtle()

size = int(input("How big do you want the sides of the inital square to be?" ))

distance = int(input("What distance do you want between the squares? "))

def square(size):
    print("Square")
    sqaureSides = 4
    while(sqaureSides > 0):
        myTurtle.forward(size)
        myTurtle.right(90)
        sqaureSides = sqaureSides - 1

def hypotenus(distance):
    print("Hyp")
    hyp = math.sqrt(distance*distance*2)
    print(hyp)
    return hyp

def invinsibleMove(hyp):
    print("Move")
    myTurtle.penup()
    myTurtle.right(45)
    myTurtle.forward(hyp)
    myTurtle.left(45)
    myTurtle.pendown()

squareNumber = 4
length = size
hyp = hypotenus(distance)
myTurtle.penup()
myTurtle.left(90)
myTurtle.forward(size/2)
myTurtle.left(90)
myTurtle.forward(size/2)
myTurtle.right(180)
myTurtle.pendown()
while(squareNumber > 0):
    sides = 4
    square(length)
    squareNumber = squareNumber -1
    length = length - 2 * distance
    invinsibleMove(hyp)
turtle.done()