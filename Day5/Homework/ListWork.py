
testList = [1,2,3,5,6,4]

#pick out largest number
largestNumber = testList[0]

for i in range(0, len(testList)):
    if(testList[i]>largestNumber):
        largestNumber = testList[i]

print(largestNumber)

#sum of the numbers in the list
totalList = 0

for i in range(0, len(testList)):
    totalList = totalList + testList[i]

print(totalList)

#multiply every number in the list
multiList = 1

for i in range(0, len(testList)):
    multiList = multiList * testList[i]

print(multiList)

#printing every third item in list
thirdList = []

for i in range(0, len(testList)):
    if((i+2) % 3 == 1):
        thirdList.append(testList[i])

print(thirdList)