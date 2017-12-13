
cardNumber = input("Type in Cardnumber: ")

doubleOfDigits = []

def numberLength(lenNumber):
    length = len(str(lenNumber))
    print(length)
    return length

def doubleAlternateDigits(number):
    for i in range(0, len(number)):
        if(i % 2 == 0):
            doubleOfDigits.append(int(number[i])*2)
        else:
            doubleOfDigits.append(int(number[i]))

def addDigits(originalNumber):
    sumNumber = 0
    while(int(originalNumber) > 0):
        sumNumber = sumNumber + originalNumber%10
        print(sumNumber)
        originalNumber = originalNumber // 10
    return sumNumber
    print(sumNumber)

normalizedAlternateNumbers = []

def validationStep2():
    for i in range (0, len(doubleOfDigits)):
        if(doubleOfDigits[i] >= 10):
            result = addDigits(doubleOfDigits[i])
            normalizedAlternateNumbers.append(result)
        else:
            normalizedAlternateNumbers.append(doubleOfDigits[i])

def validationStep3():
    sumOfAllDigits = 0
    for i in range (0, len(normalizedAlternateNumbers)):
        sumOfAllDigits += normalizedAlternateNumbers[i]
    return sumOfAllDigits

doubleAlternateDigits(cardNumber)

print(doubleOfDigits)

validationStep2()

print(normalizedAlternateNumbers)

sumOfAllDigits = validationStep3()

print("The sum of all normalized didigt is ", sumOfAllDigits)

if(sumOfAllDigits % 10 == 0):
    print("The credit card is valid.")
else:
    print("The credit card is nto valid")
