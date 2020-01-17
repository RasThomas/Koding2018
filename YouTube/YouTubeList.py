import sqlite3
import cherrypy
import json
from cherrypy import expose

def readMyDataFile(dataFile):
  with open(dataFile, encoding="utf8", mode='r') as myDataFile:
    data = json.load(myDataFile)
    return data

def musicList(jsonList):
  listP = []
  for p in jsonList:
    id = (p['snippet']['position'],p['snippet']['title'],p['snippet']['description'],p['contentDetails']['videoId'])
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

data = readMyDataFile("Music.json")

videoList = []

maxId = 0

videoList = musicList(data)

maxId = max(videoList)


idList = idList(videoList)

missingList = totalNumber(data)

missingNumbers = list(set(missingList)-set(idList))

missingNumbers.sort()

print(missingNumbers)

class PythonCafe:

    @expose
    def index(self):
        return open('HomePage.html')

    @expose
    def home(self, action):
        if action == 'Get Music':
          stringTest = ""
          stringTest = stringTest + "Test "+ "</br>"
          for i in range(len(videoList)):
              stringTest = stringTest +  "<a href=\"https://www.youtube.com/watch?v="+str(videoList[i][3])+"\">"+str(videoList[i][1])+"</a>" + "</br>"
          return stringTest;







cherrypy.quickstart(PythonCafe())
