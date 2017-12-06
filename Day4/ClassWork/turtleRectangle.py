import turtle

myTurtle = turtle.Turtle()

averageTemperatureList = [3, 4, 6, 9, 14, 17, 18, 14, 11, 7, 4]

#temperature rectangle
def setupTurtle():
    fakeTurtle = turtle.Turtle()
    fakeTurtle.penup()
    fakeTurtle.setpos(-300,0)
    fakeTurtle.pendown()
    fakeTurtle.color("red")
    fakeTurtle.pensize(2.5)

    return fakeTurtle

myTurtle = setupTurtle()

def drawRectangle():
    for i in range(0, len(averageTemperatureList)):
        myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.forward(averageTemperatureList[i] * 10)
        myTurtle.right(90)

#temperature graph
def pulse():
    for i in range(0, len(averageTemperatureList)):
        if(averageTemperatureList[i] > 10):
            myTurtle.color("green","green")
        else:
            myTurtle.color("red","red")
        myTurtle.begin_fill()
        myTurtle.left(90)
        myTurtle.forward(averageTemperatureList[i] * 10)
        myTurtle.right(90)
        myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.forward(averageTemperatureList[i] * 10)
        myTurtle.right(90)
        myTurtle.forward(20)
        myTurtle.end_fill()
        myTurtle.right(180)
        myTurtle.forward(20)
        myTurtle.end_fill()
    return myTurtle

# drawRectangle()

pulse()


test = 2017%10

print(test)

turtle.done()
