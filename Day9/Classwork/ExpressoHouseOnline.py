
import os, os.path
import random
import string

import sqlite3
import cherrypy
from cherrypy import expose

def databaseInsert(sqlStatement):
    with sqlite3.connect("expressoHouse.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(sqlStatement)
        myDatabase.commit()
        pass

def databaseExtract(sqlStatement):
    with sqlite3.connect("expressoHouse.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(sqlStatement)
        myDatabase.commit()
        rows = list(cursor.fetchall())
        print(rows)
        return rows
        pass

head = """<head>
                    <title>ExpressoHouse</title>
                     <link href="/static/css/style.css" rel="stylesheet">
                </head>"""
top = """"""
bottom = """"""

class ExpressoHouse():
    #decorate the function
    @expose
    def index(self):
        return """<html>
                """,head,"""
                  <body>
                    <div>Welcome to Expresso House</div>
                    <br /> 
                    <form method="get" action="addCustomerForm">
                      <button type="submit">Adding new customer!</button>
                    </form>
                    <br /> 
                    <form method="get" action="showCustomers">
                      <button type="submit">Show customers!</button>
                    </form>
                  </body>
                </html>"""

    @expose
    def addCustomerForm(self):
        paymentSQL = """SELECT * FROM PaymentType"""
        paymentType = databaseExtract(paymentSQL)
        payment = ""
        for i in range(0, len(paymentType)):
            pay = paymentType[i][1]
            payment = payment + "<option value='"+pay+"'>"+pay+"</option>"
        membershipSQL = """SELECT * FROM Membership"""
        membershipType = databaseExtract(membershipSQL)
        membership = ""
        for i in range(0, len(membershipType)):
            member = membershipType[i][1]
            membership = membership + "<option value='"+member+"'>"+member+"</option>"
        return """<html>
                """,head,"""
                  <body>
                    <div>Welcome to Expresso House</div>
                    <br /> 
                    <form method="get" action="addCustomer">
                        <input type="text" value="Customer Name" name="Name" /><br/>
                        <input type="text" value="Customer Adress" name="Adress" /><br/>
                        <input type="text" value="Customer Phone" name="Phone" /><br/>
                        <input type="text" value="Customer Username" name="Username" /><br/>
                        <input type="text" value="Customer Password" name="Password" /><br/>
                        <select name="PaymentType">"""+payment+"""</select><br/>   
                        <select name="MembershipType">"""+membership+"""</select><br/>  
                      <button type="submit">Adding new customer!</button>
                    </form>
                    <br /> 
                  </body>
                </html>"""

    @expose()
    def addCustomer(self, Name, Adress, Phone, Username, Password, PaymentType, MembershipClass):
        return "Customer added"

    @expose()
    def showCustomers(self):
        return "Show customers"



if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(ExpressoHouse(), '/', conf)


#http://127.0.0.1:8080/celsiusToFahrenheit?temperature=100

#Make pages for inserting into database expresso house (CRUD, create, read, update, delete), main menu with linkes?, various types of transactions and insertions, customers, purchases, etc, populate teh database, the ones without dependencies first

