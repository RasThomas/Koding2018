
def isLeapYear(year):
    leapYear = False
    if(year % 4 == 0 and year % 100 != 0):
        print("Dividable by 4 but not 100.")
        leapYear = True
    elif(year % 4 == 0 and year % 400 == 0):
        print("Dividable by 4 but also 400.")
        leapYear = True

    print(leapYear)
    return leapYear


isLeapYear(2000)
#Print all the years between two given years that are leap years DB BROWERSER SQLITE

#def printLeapYear(start, end):


#Use Dictatonary in python, state a month, get told the number

#Further, what season does that month belong to, (make 4 lists)
