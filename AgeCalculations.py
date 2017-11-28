import datetime



currentYear=int(datetime.date.today().strftime("%Y"))
correctBirth = False
#print("We are in the year ", currentYear)
while(correctBirth==False):
    birthYear = int(input("Please enter year you were born "))
    if(birthYear < 1900):
      print("That's too old!")
    elif(birthYear >= currentYear):
       print("That year is in the future")
    else:
        print("You were born in",birthYear)
        correctBirth=True
        break

futureYear = currentYear

correctFuture = False
while(correctFuture == False):
    futureYear = int(input("Please enter a year in the future "))
    if(futureYear < currentYear):
        print("You did not type in a year in the future!")

    elif(futureYear > birthYear + 120):
        print("You will probably not live beyond 120 years.")

    else:
        print(futureYear, "is in the future!")
        correctYear = True
        break

age = currentYear - birthYear

print("You are ",age," year old in the year",currentYear)

futureAge = futureYear - birthYear

print("Your age in ",futureYear," will be: ", futureAge)

if(age == 100):
    print("Congratulations on being 100 year old.")
if(age > 0 and age < 2):
    print("You are just one year old.")
if(age > 14 and age < 19):
    print("I guess you are a teenager.")

ageLength = len(str(age))
age_str = str(age)
ageLast = int(age_str[ageLength -1])
#print("Last number in age ", ageLast)

if(ageLast == 0):
    print("You are", age, "old and have started a new decade.")

birth_str = str(birthYear)
yearLength = len(birth_str)
year_str = str(yearLength)
yearNumber = int(year_str)
yearTotal = 0
#print("Number of digits", yearNumber, " year ", birth_str)

while(yearNumber > 0):
   # print(birth_str[yearNumber-1])
    numberYear = int(birth_str[yearNumber-1])
    yearTotal = yearTotal + numberYear
    yearNumber = yearNumber -1
    #print(yearTotal)

print("The total sum of years of the birthyear is",yearTotal,".")
