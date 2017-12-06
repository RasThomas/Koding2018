import turtle

myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
mySecondTurtle = turtle.Turtle()

myList = [1,2,3,5,8]

print(myList)

print(myList[0])

print(myList[4])

#print(myList[5])


#defining the function
def printMyList(listS):
    print("In the function")
    for i in range (0, len(listS)):
        print(listS[i]),

#Calling he fucntion
printMyList(myList)

number = 13

#adding a number to myList
def addNumber(number):
    print("Adding ", number," to myList.")
    myList.append(number)


addNumber(number)

printMyList(myList)

#sum of myList
def sumList():
    sumOfList = 0
    print("Summing up my list of numbers")
    for i in range(0, len(myList)):
        sumOfList = sumOfList + myList[i]
    print("The sum of myList is ", sumOfList)

sumList()

def usingTurtleWithLists():
    for i in range(0, len(myList)):
        myTurtle.forward(i*10)
        myTurtle.right(90)

usingTurtleWithLists()

usingTurtleWithLists()


bochList = [1]

#generates Fibonacci(?) numbers
def makeList(lengthList):
    prevNumber = 1
    prevNumber2 = 1
    currentNumber = 1
    print("Making an ", lengthList+1, " number long Fibonacci list.")
    for i in range (0, int(lengthList)):

        currentNumber = prevNumber + prevNumber2
        bochList.append(currentNumber)
        prevNumber2 = prevNumber
        prevNumber = currentNumber

listLength = int(input("Number for length of list"))-1

makeList(listLength)

printMyList(bochList)

turtle.done()
