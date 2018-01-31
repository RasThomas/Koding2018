
import sqlite3

def insertIntoTable(createSQL):
    with sqlite3.connect("expressoHouse.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(createSQL)
        myDatabase.commit()
        pass

#insertSql = """INSERT INTO customer VALUES ("NULL, "Drew Barrymore", "5006, Bergen", 238923892, "drew.arrymore", "123456",1,1)"""

insertSql = """INSERT INTO customer (Name, Adress, Phone, Username, Password, PaymentTypeid, Membershipid) VALUES ("Drew Barrymore", "5006, Bergen", 238923892, "drew.barrymore", "123456",1,1)"""

#insertIntoTable(insertSql)

def instertIntoCustomerTable(item):
    customer = """INSERT INTO customer (Name, Adress, Phone, Username, Password, PaymentTypeid, Membershipid) VALUES ("""+item+""")"""
    print(customer)
    insertIntoTable(customer)
    pass

instertIntoCustomerTable('"Drew Barrymore","5006, Bergen", 453135435,"drew.Barrymore", "123456", 1, 2')

def getDataFromTable(createSQL):
    with sqlite3.connect("ExpressoHouse.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(createSQL)
        myDatabase.commit()
        rows = cursor.fetchall()

        for row in rows:
            print(row)
        pass

getSQL = """SELECT * FROM customer"""

getDataFromTable(getSQL)
