

import sqlite3

def insertIntoTable(createSQL):
    with sqlite3.connect("ShoeStore.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(createSQL)
        myDatabase.commit()
        pass

insertQuery = """INSERT INTO Customer VALUES (1, "Thomas", "03.05.82", "5209, Os", 91135369)"""

insertIntoTable(insertQuery)

