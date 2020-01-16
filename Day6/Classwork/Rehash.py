myNumber = int(input("Enter a number"))

sumOfDigits = 0

while myNumber > 0:
    sumOfDigits = sumOfDigits + myNumber % 10
    myNumber = int (myNumber /10)
    print("sumOfDigits =", sumOfDigits, " myNumber = ", myNumber)

print("Sum of Didigts is", sumOfDigits)

myList = [1,2,["a","b","c*"],5.0,-6.0]

def listing(testList):
    for i in range(0, len(testList)):
        if(isinstance(testList[i],list)):
            listing(testList[i])
        else:
            print(testList[i],type(testList[i]))

listing(myList)

def arealRectangle(length, width):
    areal = length * width
    return areal

size = arealRectangle(3,2)

print(size)