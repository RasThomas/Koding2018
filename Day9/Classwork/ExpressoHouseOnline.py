
import os, os.path
import random
import string

import cherrypy
from cherrypy import expose


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
                        <input type="text" value="Payment Type" name="PaymentType" /><br/>
                        <input type="text" value="Membership Class" name="MembershipClass" /><br/>
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

