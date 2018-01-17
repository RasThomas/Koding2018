

testList=[1,2,5,0,-1, 21, 15, 7, 200, -9]

def maxInAList(myList):
    maxNumber = myList[0]
    for i in range (0, len(myList)):
        if maxNumber < myList[i]:
            maxNumber = myList[i]
            print("Max number is now ", maxNumber)
    return maxNumber


maxInAList(testList)

def longestWord(myList):
    longestWord = ""
    for i in range (0, len(myList)):
        if len(longestWord) < len(myList[i]):
            longestWord = myList[i]
            print("The longest word currently is ",longestWord, "with ",len(longestWord), "letters.")
    return longestWord

def readMyDataFile(dateFile):
    with open(dateFile, mode ='r') as myDataFile:
        item = myDataFile.read().splitlines()
        print(type(item))
        print(item)
        return item

newList = readMyDataFile("moreData.txt")

longestWord(newList)

#write function to count the number of occurances of a word in a file
