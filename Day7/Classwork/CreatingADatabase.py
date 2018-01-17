#sqlite brower org

import sqlite3

def crateTable(createSQL):
    with sqlite3.connect("ShoeStore.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(createSQL)
        myDatabase.commit()
        pass



createSql = """CREATE TABLE `Customer` ( `CustomerId` INTEGER, `Name` TEXT, `DateOfBirth` TEXT, `Adress` TEXT, `PhoneNumber` INTEGER, PRIMARY KEY(`CustomerId`) )"""

crateTable(createSql)

