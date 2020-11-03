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

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    s1 = _datetime.date(y1, m1, d1)
    s2 = _datetime.date(y2, m2, d2)
    u1 = time.mktime(_datetime.datetime.strptime(str(s1), "%Y-%m-%d").timetuple()) 
    u2 = time.mktime(_datetime.datetime.strptime(str(s2), "%Y-%m-%d").timetuple()) 
    if(u2 < u1):
        print("Error. Date Two is before Date One")
    # Total days
    days = ((u2 - u1) / 86400)
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
    
testDaysBetweenDates()