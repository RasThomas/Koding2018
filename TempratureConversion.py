

fahrInput = int(input("Type in temrature in Fahrenheit for conversion to Celsius. "))

celInput = int(input("Type in temprature in Celsius for conversion to Fahrenheit. "))

celConv = (((fahrInput - 32)/9) * 5)

fahrConv = (((celInput * 9) + 160)/5)

print(fahrInput, " in Fahrenheit is ",celConv, " in Celsius")

print(celInput, " in Celsius is ",fahrConv, " in Fahrhenheit")

#Defining a function
def celciusToFahrenheit():
    myInput = int(input("Enter a temperature in Celsius :"))
    tempInFahrenheit = (((celInput * 9) + 160)/5)
    print("The temperature of ",myInput, "in celsius is ",tempInFahrenheit," in Fahrenheit")

def fahrenheitToCelsius():
    myInput = int(input("Enter a temperature in Fahrenheit :"))
    tempInCelsius = (((fahrInput - 32)/9) * 5)
    print("The temperature of ", myInput, "in fahrenheit is ", tempInCelsius," in Celsius")

#Calling a function

celciusToFahrenheit()
fahrenheitToCelsius()
