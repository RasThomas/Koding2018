import turtle

myTurtle = turtle.Turtle()

averageTemperatureList = [3, 4, 6, 9, 14, 17, 18, 14, 11, 7, 4]

def drawRectangle():
    for i in range(0, len(averageTemperatureList)):
        myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.forward(averageTemperatureList[i]* 10)
        myTurtle.right(90)



def pulse():
    for i in range(0, len(averageTemperatureList)):
        myTurtle.left(90)
        myTurtle.forward(averageTemperatureList[i]* 10)
        myTurtle.right(90)
        myTurtle.forward(20)
        myTurtle.right(90)
        myTurtle.forward(averageTemperatureList[i]* 10)
        myTurtle.left(90)


#drawRectangle()

pulse()

turtle.done()
