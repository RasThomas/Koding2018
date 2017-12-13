import math

testList = [3, 4, 6, 9, 14, 17, 18, 14, 11, 7, 4]

#first task
sumList = 0

for i in range(0, len(testList)):
    sumList = sumList + testList[i]

print(sumList)

#second task
multiList = 1

for i in range(0, len(testList)):
    if(testList[i]!=0):
        multiList = multiList * testList[i]

print(multiList)

#third task
largestNumber = 0

for i in range(0, len(testList)):
    if(testList[i] > largestNumber):
        largestNumber = testList[i]

print(largestNumber)

#fourth task
thirdList = testList[3::3]

for i in range(0, len(thirdList)):
    print(thirdList[i])

#fifth task
firstAngle = int(input("Type in the first angle: "))

secondAngle = int(input("Type in second angle: "))

hypotenuse = math.sqrt(firstAngle * firstAngle + secondAngle * secondAngle)

print(hypotenuse)