import math

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

#write function to count the number of occurances of a word in a file (List up occurances of each word?, new list with 2 part lsit with word and count?)
def countWord(word, fileName):
    wordList = []
    with open(fileName, mode = 'r') as myDateFile:
        wordList = myDateFile.read().split()
        print(wordList)
    wordCount = 0
    for i in range (0, len(wordList)):
        if (word.upper() == wordList[i].upper()):
            wordCount= wordCount+1
    print("The ",word, "was found ",wordCount, "times.")


countWord("og", "textFile.txt")

#plane takes off at at 60 angle, after 25 km, what is height?
def planeHeight(angle, distance):
    length = distance * math.sin(math.radians(angle)) #convert from angle to radius
    length = format(length,'.2f') # limit to 2 decimals
    print("The plane have reached a height of",length,"km after flying 25 km at a 60 degree angle.")
    return length

planeHeight(60, 25)