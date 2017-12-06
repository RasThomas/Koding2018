

myList = [1,2,3,5,8]

print(myList)

print(myList[0])

print(myList[4])

#print(myList[5])
def makeList(lengthList):
    print("Making an ", lengthList, " number long Bochelli list.")

#defining the function
def printMyList():
    print("In the function")
    for i in range (0, len(myList)):
        print(myList[i], ".")

#Calling he fucntion
printMyList()

number = 13

#adding a number to myList
def addNumber(number):
    print("Adding ", number," to myList.")
    myList.append(number)

addNumber(number)

printMyList()

#sum of myList
def sumList():
    sumOfList = 0
    print("Summing up my list of numbers")
    for i in range(0, len(myList)):
        sumOfList = sumOfList + myList[i]
    print("The sum of myList is ", sumOfList)

sumList()

