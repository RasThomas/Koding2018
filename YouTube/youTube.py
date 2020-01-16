import json

def readMyDataFile(dataFile):
  with open(dataFile, encoding="utf8", mode='r') as myDataFile:
    data = json.load(myDataFile)
    return data

data = readMyDataFile("Music.json")

videoList = []
maxId = 0

def numberList(jsonList):
  listP = []
  for p in jsonList:
    id = (p['snippet']['position'])
    print(id)
    listP.append(id)
  return listP

videoList = numberList(data)

maxId = max(videoList)

def missingNumber(list):
  missingList = []
  p = 0
  while p < maxId:
    missingList.append(p)
    p = p +1
  return missingList

missingList = missingNumber(data)

print((list(set(missingList)-set(videoList))))





