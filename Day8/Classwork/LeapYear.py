
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

def printLeapYear(start, end):
    leapYears = []
    if(start > end):
        print("Start year cant be greater than end year")
    else:
        year = start
        while (year < end):
            if(isLeapYear(year) == True):
                leapYears.append(year)
                print(year, "is a leap year.")
            else:
                print(year, "is not a leap year.")
            year = year +1
        print("The following years are leap years:")
        for j in range (0, len(leapYears)):
            print(leapYears[j])
    return leapYears

printLeapYear(1900, 2000)

def daysInAMonth(month):
    months = {"January": 31, "February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"Desember":31}
    days = months[month]
    print(days)
    return days

daysInAMonth("May")

#Further, what season does that month belong to, (make 4 lists)

def seasonOfAMonth(month):
    seasons = {"January": "Winter", "February":"Winter","March":"Spring","April":"Spring","May":"Spring","June":"Summer","July":"Summer","August":"Summer","September":"Fall","October":"Fall","November":"Fall","Desember":"Winter"}
    season = seasons[month]
    print(season)
    return season

seasonOfAMonth("May")