import datetime

birthYear = int(input("Please enter year you were born "))

currentYear=int(datetime.date.today().strftime("%Y"))

#print("We are in the year ", currentYear)

if(birthYear < 1900):
    print("That's too old!")
    exit()
elif(birthYear >= currentYear):
    print("That year is in the future")
    exit()

futureYear = int(input("Please enter a year in the future "))

if(futureYear < currentYear):
    print("You did not type in a year in the future!")
    exit()
elif(futureYear > currentYear + 120):
    print("You will probably not live beyond 120 years.")
    exit()

age = currentYear - birthYear

print("You are ", age, " in this year. ")

futureAge = futureYear - birthYear

print("Your age in ", futureYear, " will be: ", futureAge)

if(age == 100):
    print("Congratulations on being 100 year old.")
if(age > 0 and age < 2):
    print("You are just one year old.")
if(age > 14 and age < 19):
    print("I guess you are a teenager.")

ageLength = len(str(age))
age_str = str(age)
ageLast = int(age_str[ageLength -1])
print("Last number in age ", ageLast)

if(ageLast == 0):
    print("You are ", age, "old and have started a new decade.")

birth_str = str(birthYear)
yearLength = len(birth_str)
year_str = str(yearLength)
yearNumber = int(year_str)
yearTotal = 0
print("Number of digits", yearNumber, " year ", birth_str)

while(yearNumber > 0):
    print(birth_str[yearNumber-1])
    numberYear = int(birth_str[yearNumber-1])
    yearTotal = yearTotal + numberYear
    yearNumber = yearNumber -1
    print(yearTotal)

print("The total sum of years of the birthyear is ",yearTotal,".")
