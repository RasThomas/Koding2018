

import sqlite3

def updateTable(createSQL):
    with sqlite3.connect("ShoeStore.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(createSQL)
        myDatabase.commit()
        pass

insertQuery = """UPDATE Customer SET PhoneNumber = 12345678 WHERE CustomerID = 1;"""

updateTable(insertQuery)
