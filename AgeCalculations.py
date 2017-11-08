import datetime

birthYear = int(input("Please enter year you were born"))

currentYear=int(datetime.date.today().strftime("%Y"))

#print("We are in the year ", currentYear)

if(birthYear < 1900):
    print("That's too old!")
    exit()
elif(birthYear >= currentYear):
    print("That year is in the future")
    exit()

futureYear = int(input("Please enter a year in the future"))

if(futureYear < currentYear):
    print("You did not type in a year in the future!")
    exit()
elif(futureYear > currentYear + 120):
    print("You will probably not live beyond 120 years.")
    exit()

print("My age in ", futureYear, " will be: ", futureYear-birthYear)

#Tasks for homework
# 1) What f its a new born baby? Greet him/her. :)
# 2)
