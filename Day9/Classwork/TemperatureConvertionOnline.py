
import cherrypy
from cherrypy import expose

class TemperatureConverter():
    #decorate the function
    @expose
    def index(self):
        return """<html>
                  <head></head>
                  <body>
                    <div> Temperature Convertion <div>
                    <br /> 
                    <form method="get" action="celsiusToFahrenheit">
                      <input type="text" value="0" name="temperature" />
                      <button type="submit">Celsius to Fahrenheit!</button>
                    </form>
                    <br /> 
                    <form method="get" action="fahrenheitToCelsius">
                      <input type="text" value="0" name="temperature" />
                      <button type="submit">Fahrenheit to Celsius!</button>
                    </form>
                  </body>
                </html>"""

    @expose
    def celsiusToFahrenheit(self, temperature):
        tempInFahrenheit = (((int(temperature) * 9) + 160)/5)
        returnStr = "The temperature of ",str(temperature), "in celsius is ",tempInFahrenheit," in fahrenheit"
        return str(returnStr)

    @expose()
    def fahrenheitToCelsius(self, temperature):
        tempInCelsius = (((int(temperature) - 32)/9) * 5)
        print("The temperature of ", temperature, "in fahrenheit is ", tempInCelsius," in celsius")
        return str(tempInCelsius)


if __name__ == '__main__':
    cherrypy.quickstart(TemperatureConverter())

#http://127.0.0.1:8080/celsiusToFahrenheit?temperature=100

#Make pages for inserting into database expresso house (CRUD, create, read, update, delete), main menu with linkes?, various types of transactions and insertions, customers, purchases, etc, populate teh database, the ones without dependencies first

