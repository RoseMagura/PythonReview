import time
import _datetime
# Given your birthday and the current date, calculate your age in days.
# Compensate for leap days. Assume that the birthday and current date are
# correct dates (and no time travel). Simply put, if you were born on
# January 1st 2012 and today's date is January 2nd 2012, you are 1 
# day old.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

def isLeapYear(year): 
    if(year % 4 == 0):
        return True
    else: 
        return False

def getDate(year, month, day):
    try:
        return _datetime.date(year, month, day)
    except ValueError:
        print("Oops! That is not a valid date. Please try again.")
        return None   

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    date1 = getDate(y1, m1, d1)
    date2 = getDate(y2, m2, d2)
    u1 = time.mktime(_datetime.datetime.strptime(str(date1), "%Y-%m-%d").timetuple())
    u2 = time.mktime(_datetime.datetime.strptime(str(date2), "%Y-%m-%d").timetuple()) 
    if(u2 < u1):
        print("Error. Date Two is before Date One.")
        return None
    # Total days
    days = ((u2 - u1) / 86400)
    return days

def nextDay(y, m, d):
    if m == 2 and d == 28 and isLeapYear(y):
            return getDate(y, m, 29)
    elif d < daysOfMonths[m - 1]:
        return getDate(y, m, d + 1)
    else:
        if m < 12:
            return getDate(y, m + 1, 1)
        else:
            return getDate(y + 1, 1, 1)

def daysBetweenDatesAlgorithm(y1, m1, d1, y2, m2, d2):
    days = 0
    d1 = getDate(y1, m1, d1)
    d2 = getDate(y2, m2, d2)
    if d2 < d1 :
        return "Error. Date Two is before Date One. Please try again."
    while d1 < d2:
        d1 = nextDay(d1.year, d1.month, d1.day)
        days += 1
    return days

def testDaysBetweenDates():
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)

    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)

    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)


    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
# testDaysBetweenDates() 
# print(daysBetweenDates(2012, 6, 29, 2012, 6, 30))
# print(daysBetweenDatesAlgorithm(1912, 12, 12, 2012, 12, 12))
print(daysBetweenDatesAlgorithm(2013, 1, 1, 2012, 12, 20))