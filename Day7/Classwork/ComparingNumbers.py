import math
import operator

testList=[1,2,5,0,-1, 21, 15, 7, 200, -9]

def maxInAList(myList):
    maxNumber = myList[0]
    for i in range (0, len(myList)):
        if maxNumber < myList[i]:
            maxNumber = myList[i]
#            print("Max number is now ", maxNumber)
    return maxNumber


print(maxInAList(testList))

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
        if (word.upper() == wordList[i].upper()): #to ignore the difference in words with upper and lower case
            wordCount= wordCount+1
    print("The word",word, "was found ",wordCount, "times.")

def countWOrds(fileName):
    wordList = []
    with open(fileName, mode = 'r') as myDateFile:
        wordList = myDateFile.read().split()
#        print(wordList)
    countedWords = [[wordList[0].upper().replace(',', '').replace('.', ''),0]]
#    print(countedWords)
    for i in range (0, len(wordList)):
        found = False
        for j in range (0, len(countedWords)):
            if (wordList[i].upper() == countedWords[j][0]):
                counted = countedWords[j][1] +1
                countedWords[j][1] = counted
#                print(countedWords[j][0], "been found ",counted, "times.")
                found = True
                break
        if(found != True):
            newWord = wordList[i].upper().replace(',', '')
            countedWords.append([newWord, 1])
#            print("New word ", newWord)


    print(sorted(countedWords, key=operator.itemgetter(1), reverse=True))

countWOrds("textFile.txt")



countWord("og", "textFile.txt")

#plane takes off at at 60 angle, after 25 km, what is height?
def planeHeight(angle, distance):
    length = distance * math.sin(math.radians(angle)) #convert from angle to radius
    length = format(length,'.2f') # limit to 2 decimals
    print("The plane have reached a height of",length,"km after flying 25 km at a 60 degree angle.")
    return length

planeHeight(60, 25)
