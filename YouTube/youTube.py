import json
import sqlite3

DB_NAME = "youtube.db"

def readMyDataFile(dataFile):
  with open(dataFile, mode='r') as myDataFile:
    data = json.load(dataFile)
    return data


def writeMyDataFile(fileData, fileName):
  with open(fileName, mode='w') as myDataFile:
    for club in fileData:
      myDataFile.write(club + '\n')
    print(fileData)


def insertDataIntoTable(dbName, item, sql):
  with sqlite3.connect(dbName) as db:
    cursor = db.cursor()
    cursor.execute(sql, item)
    db.commit()


def readTableItems(dbName, sql):
  with sqlite3.connect(dbName) as db:
    cursor = db.cursor()
    # sql = 'SELECT * FROM Music'
    cursor.execute(sql)
    items = cursor.fetchall()
    print(items)
    db.commit()
    return items


def updateTable(createSQL, dataBase):
  with sqlite3.connect(dataBase) as myDatabase:
    cursor = myDatabase.cursor()
    cursor.execute(createSQL)
    myDatabase.commit()
    pass

videoList = []

maxId = 0

def readMyDataFile(dataFile):
  with open(dataFile, encoding="utf8", mode='r') as myDataFile:
    data = json.load(myDataFile)
    return data

def musicList(jsonList):
  listP = []
  for p in jsonList:
    id = (p['snippet']['position'],p['snippet']['description'],p['snippet']['title'])
#    print(id)
    global maxId
    if(p['snippet']['position'] > maxId):
      maxId = int(p['snippet']['position'])
    listP.append(id)
  return listP

def totalNumber(list):
  missingList = []
  p = 0
  while p < maxId[0]:
    missingList.append(p)
    p = p +1
  return missingList

def idList(fullList):
  idList = []
  for x in fullList:
    idList.append(x[0])
  return idList

def searchList(string, list):
  hitList = []
  searchTerm = string
  for x in range(len(list)):
    if searchTerm.casefold() in list[x][2].casefold():
      hitList.append(list[x][2])
      print(list[x][2])
  return hitList


data = readMyDataFile("Music.json")



videoList = musicList(data)

maxId = max(videoList)


idList = idList(videoList)

missingList = totalNumber(data)

missingNumbers = list(set(missingList)-set(idList))

missingNumbers.sort()

print(missingNumbers)

searchList("Scott", videoList)



