import math

def divideAndSummerize(originalNumber):
    sumNumber = 0
    while(int(originalNumber) > 0):
        sumNumber = sumNumber + originalNumber%10
        print(sumNumber)
        originalNumber = originalNumber // 10

    print(sumNumber)

myNumber = int(input("Enter a number: "))

divideAndSummerize(myNumber)

