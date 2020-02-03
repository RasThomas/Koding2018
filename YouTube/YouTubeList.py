import sqlite3
import cherrypy
import json
from cherrypy import expose
from mako.template import Template

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

def searchList(string, list):
  hitList = []
  searchTerm = string
  for x in range(len(list)):
    if searchTerm.casefold() in list[x][1].casefold():
      hitList.append(list[x])
      print(list[x][1])
  return hitList


data = readMyDataFile("Music.json")

videoList = []

maxId = 0

videoList = musicList(data)

def sortSecond(val):
    return val[1]

titleList = videoList

titleList.sort(key = sortSecond)

maxId = max(videoList)


idList = idList(videoList)

missingList = totalNumber(data)

missingNumbers = list(set(missingList)-set(idList))

missingNumbers.sort()

print(missingNumbers)

stringTest = ""

searchString = ""

class YouTubeList:

    @expose
    def index(self):
        return Template(filename='HomePage.html').render(table="")

    @expose
    def musicSearch(self,inputName):
        stringTest = inputName
        stringTest = stringTest + "Test " + "</br>"
        for i in range(len(titleList)):
            stringTest = stringTest + "<a href=\"https://www.youtube.com/watch?v=" + str(titleList[i][3]) + "\">" + str(
                titleList[i][1]) + "</a>" + "</br>"
        table = stringTest;
        print("MuslicList")
        return Template(filename='HomePage.html').render(table=table)



    @expose
    def search(self, action, searchItem):

        if action == 'Search Music':
            if len(searchItem) < 3:
                table = "Search must have 3 characters."
            else:
                hitList = searchList(searchItem, videoList)
                searchString = ""
                searchString = searchString + "Search " + "</br>"
                for i in range(len(hitList)):
                    searchString = searchString + "<a href=\"https://www.youtube.com/watch?v=" + str(hitList[i][3]) + "\">" + str(
                        hitList[i][1]) + "</a>" + "</br>"
                table = searchString;
                print("MuslicList")
            return Template(filename='HomePage.html').render(table=table)

    @expose
    def home(self, action):
        if action == 'Get Music':
            print("Get Music")
            musicString = ""
            musicString = musicString + "Videoliste "+ "</br>"
            for i in range(len(titleList)):
                musicString = musicString +  "<a href=\"https://www.youtube.com/watch?v="+str(titleList[i][3])+"\">"+str(titleList[i][1])+"</a>" + "</br>"
            return Template(filename='HomePage.html').render(table=musicString)
        if action == 'Missing numbers':
            print("Missing numbers")
            missingMusic = ""
            missingMusic = missingMusic + "Numbers missing in youtube list "+ "</br>"
            print(missingNumbers)
            print(missingNumbers[1])
            for i in range(len(missingNumbers)):
                missingMusic = missingMusic + str(missingNumbers[i])+ "</br>"
            return Template(filename='HomePage.html').render(table=missingMusic)
        if action == 'Private or deleted video':
            print("Private or deleted video")
            searchString = ""
            fullList = []
            privateList = searchList("Private video", videoList)
            deletedList = searchList("Deleted video", videoList)
            fullList = privateList + deletedList
            for i in range(len(fullList)):
                searchString = searchString + "<a href=\"https://www.youtube.com/watch?v=" + str(fullList[i][3]) + "\">" + str(
                    fullList[i][1]) + "</a>" + "</br>"
            table = searchString;
            print("MuslicList")
            return Template(filename='HomePage.html').render(table=table)







cherrypy.quickstart(YouTubeList())
