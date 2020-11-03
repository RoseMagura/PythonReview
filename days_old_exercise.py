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
    # Days from years
    leapYears = 0

    if isLeapYear(y1):
        leapYears += 1
    if isLeapYear(y2):
        leapYears += 1
    # print("y1 leap? " + str(isLeapYear(y1)))
    # print("y2 leap? " + str(isLeapYear(y2)))
    years = (y2 - y1) 

    # years = 0

    print("years: " + str(years))
    # print("before: " + str(leapYears))
    leapYears += int(years / 4)
    # print(int(years / 4))
    # print("after: " + str(leapYears))
    print("number of leap years: " + str(leapYears))
    # yearDays = leapYears * 366 + (years - leapYears) * 365
    yearDays = years * 365 + leapYears

    # Days from months
    m1Days = daysOfMonths[m1 - 1]
    m2Days = daysOfMonths[m2 - 2]
    # print("m1: " + str(m1) + " m2: " + str(m2)) 
    slice = daysOfMonths[(m1 - 1) : (m2 - 1)]
    # print("month days: " + str(sum(slice)))

    # Total days
    days = yearDays + sum(slice) + (d2 - d1)
    return days

def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)


    # test new year
    # assert(daysBetweenDates(2017, 12, 30, 
    #                           2018, 1,  1)  == 2)


    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
# testDaysBetweenDates()
print(daysBetweenDates(2017, 12, 30, 2018, 1, 1))