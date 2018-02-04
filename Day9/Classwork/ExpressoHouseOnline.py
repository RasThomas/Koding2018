
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
                    <form method="get" action="addOrder">
                      <button type="submit">Adding new order!</button>
                    </form>
                    <br /> 
                    <form method="get" action="showCustomers">
                      <button type="submit">Show customers!</button>
                    </form>
                    <br /> 
                    <form method="get" action="addCustomerForm">
                      <button type="submit">Adding new customer!</button>
                    </form>
                    <br /> 
                    <form method="get" action="searchCustomers">
                      <button type="submit">Search customers!</button>
                    </form>
                    <br /> 
                    <form method="get" action="products">
                      <button type="submit">Products!</button>
                    </form>
                    <br /> 
                    <br /> 
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
                        <input type="text" value="Customer Name" name="personName" /><br/>
                        <input type="text" value="Customer Adress" name="adress" /><br/>
                        <input type="text" value="Customer Phone" name="phone" /><br/>
                        <input type="text" value="Customer Username" name="username" /><br/>
                        <input type="text" value="Customer Password" name="password" /><br/>
                        <select name="paymentTypeid">"""+payment+"""</select><br/>   
                        <select name="membershipid">"""+membership+"""</select><br/>  
                      <button type="submit">Adding new customer!</button>
                    </form>
                    <br /> 
                  </body>
                </html>"""

    @expose()
    def addCustomer(self,personName, adress, phone, username, password, paymentTypeid, membershipid):
        customer = """INSERT INTO Customer (Name, Adress, Phone, Username, Password, PaymentTypeid, Membershipid) VALUES ("""+personName+""", "5006, Bergen", 238923892, "drew.barrymore", "123456",1,1)"""
        print(customer)
        databaseInsert(customer)
        pass
        return "Customer added"

    @expose()
    def showCustomers(self):
#        showCustomer = """SELECT c.Name, c.Adress, c.Phone, c.Username, p.NameOfPayment, m.MembershipName from Customer c JOIN PaymentType p ON c.MembershipID = m.Membershipid JOIN Membership m  ON c.PaymentTypeID=p.PaymentTypeid"""
        showCustomer = """SELECT c.Name, c.Adress, c.Phone, c.Username from Customer c """
        print(showCustomer)
        showCust = databaseExtract(showCustomer)
        table = ""
        for i in range(0, len(showCust)):
            table = table+ "<tr>"
            for j in range(0, len(showCust[i])):
                tableContent = str(showCust[i][j])
                table = table + "<th>"+tableContent+"</th>"
            table = table + "</tr>"
        return """<html>
                """, head, """
                  <body>
                    <div>Welcome to Expresso House</div>
                    <br /> 
                     <table style="width:100%">
                      <tr>
                        <th>Name</th>
                        <th>Adress</th>
                        <th>Phone</th>
                        <th>Username</th>
                        <th>Payment Type</th>
                        <th>Membership Type</th>
                      </tr>
                    """+table+"""
                    </table> 

                                        
                  </body>
                </html>"""
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

