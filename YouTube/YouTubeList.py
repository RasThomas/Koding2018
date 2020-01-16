import sqlite3
import cherrypy
import json
from cherrypy import expose

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

class PythonCafe:

    @expose
    def index(self):
        return open('HomePage.html')







cherrypy.quickstart(PythonCafe())
