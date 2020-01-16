import random

finalTally = 0

dices = int(input("Number of dices:"))

while(dices > 0):
    dice = random.randint(1,6)
    finalTally = finalTally+dice
    dices = dices-1

print(finalTally)

minimumNumber = int(input("What is the minimum number?"))
maxNumber = int(input("What is the maximum number?"))
myRandomNumber = random.randint(minimumNumber,maxNumber)

theNumbeGuessed = int(input("Guess a number between "+ str(minimumNumber)+ " and "+ str(maxNumber)+ ": "))

tries = 0
maxTries = 6

while (tries < maxTries):
    if(theNumbeGuessed != myRandomNumber):
        print("Wrong, guess again.")
        tries = tries + 1
        theNumbeGuessed = int(input("Guess again!"))
    elif(theNumbeGuessed == myRandomNumber):
        print("Correct!")
        break
else:
    print("Out of attemts!")

# What if we are adding numbers outside range
# Make a way to continue playing the game

print(myRandomNumber)
