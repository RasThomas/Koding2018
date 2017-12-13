import turtle

myTurtle = turtle.Turtle()

averageTemperatureList = [3, 4, 6, 9, 14, 17, 18, 14, 11, 7, 4]
numberOfRainyDays = [22, 19, 19, 18, 17, 18, 19, 19, 20, 21, 21, 20]

#temperature rectangle
def setupTurtle():
    fakeTurtle = turtle.Turtle()
    fakeTurtle.penup()
    fakeTurtle.setpos(-300,0)
    fakeTurtle.pendown()
    fakeTurtle.color("red")
    fakeTurtle.pensize(2.5)
    fakeTurtle.speed()

    return fakeTurtle

myTurtle = setupTurtle()

def drawRectangle():
    for i in range(0, len(averageTemperatureList)):
        myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.forward(averageTemperatureList[i] * 10)
        myTurtle.right(90)

#temperature graph
def pulse(listUsed, type):
    for i in range(0, len(listUsed)):
        if(type=="temp"):
            if(listUsed[i] > 10):
                myTurtle.color("green","green")
            else:
                myTurtle.color("red","red")
        elif(type=="rain"):
            myTurtle.color("blue","blue")
        myTurtle.begin_fill()
        myTurtle.left(90)
        myTurtle.forward(listUsed[i] * 10)
        myTurtle.right(90)
        myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.forward(listUsed[i] * 10)
        myTurtle.right(90)
        myTurtle.forward(20)
        myTurtle.end_fill()
        myTurtle.right(180)
        myTurtle.forward(20)
        myTurtle.end_fill()
    return myTurtle

def tempCircle(tempList):
    myTurtle.forward(50)
    for i in range(0, len(tempList)):
        temp=tempList[i]*5
        if(tempList[i] > 10):
            myTurtle.color("green","green")
        else:
            myTurtle.color("red","red")
        myTurtle.penup()
        myTurtle.right(90)
        myTurtle.forward((temp/2))
        myTurtle.pendown()
        myTurtle.circle(tempList[i])
        myTurtle.penup()
        myTurtle.right(180)
        myTurtle.forward((temp/2))
        myTurtle.right(90)
        myTurtle.pendown()

# drawRectangle()

pulse(averageTemperatureList, "temp")

pulse(numberOfRainyDays,"rain")

tempCircle(averageTemperatureList)

test = 2017%10

print(test)

turtle.done()
