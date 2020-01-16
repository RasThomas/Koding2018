import turtle

# fahrInput = int(input("Type in temrature in Fahrenheit for conversion to Celsius. "))
#
# celInput = int(input("Type in temprature in Celsius for conversion to Fahrenheit. "))
#
# celConv = (((fahrInput - 32)/9) * 5)
#
# fahrConv = (((celInput * 9) + 160)/5)
#
# print(fahrInput, " in Fahrenheit is ",celConv, " in Celsius")
#
# print(celInput, " in Celsius is ",fahrConv, " in Fahrhenheit")





#Defining a function
def celciusToFahrenheit():
    myInput = (input("Enter a temperature in Celsius :"))
    # trueTemp = False
    # while(trueTemp == False):
    #     myInput = (input("Enter a temperature in Celsius :"))
    #     print(isinstance(int(myInput), int))
    #     if(isinstance(myInput, int)==True):
    tempInFahrenheit = (((float(myInput) * 9) + 160)/5)
    print("The temperature of ",myInput, "in celsius is ",tempInFahrenheit," in Fahrenheit")
    turtleSqare(tempInFahrenheit)
        #     trueTemp = True
        # else:
        #     print("Type in a correct value")


def fahrenheitToCelsius():
    myInput = float(input("Enter a temperature in Fahrenheit :"))
    tempInCelsius = (((myInput - 32)/9) * 5)
    print("The temperature of ", myInput, "in fahrenheit is ", tempInCelsius," in Celsius")
    turtleSqare(tempInCelsius)

def isInt(test):
    isinstance(test, int)

def turtleSqare(temp):
    myTurtle = turtle.Turtle()
    sides = 4
    print(sides)
    while(sides > 0):
        myTurtle.forward(temp*10)
        myTurtle.right(90)
        sides = sides - 1
    turtle.exitonclick()



#Calling a function

#celciusToFahrenheit()
#fahrenheitToCelsius()



tempTrue = False

while(tempTrue == False):
    tempType = input("Type F for convertion to Fahrenheit and C for convertion to Celsius: ")
    if(tempType == "F" or  tempType == "f"):
        celciusToFahrenheit()
        tempTrue=True
    elif(tempType == "C" or  tempType == "c"):
        fahrenheitToCelsius()
        tempTrue=True
    else:
        print("You did not type in correct letter!")


