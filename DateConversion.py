def getDayofYear(dt):
    l = dt.split("/")
    year = int(l[2])
    month = int(l[1])
    date = int(l[0])
    day = 0
    
    for i in range (1, month):
        if i in [1,3,5,7,8,10,12]:
            day += 31
        elif i == 2:
            if i % 2 == 0: 
                day += 29
            else:
                day += 28
        else:
            day += 30
    day += date
    
    newdt = year * 1000 + day
    return newdt

def parseDate(s):
    d, m, y = s.split('/')
    return int(d), int(m), int(y)

def ddmm2ddd(m ,d):
    daysinMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    cumDaysinMonth = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 274, 304, 335, 365]
    return dd + cumDaysinMonth[mm]

def isLeap(y):
    if y % 100 == 0:
        y = y // 100
    return y % 4 == 0

def to Julian(dateStr):
    dd, mm, y4 = parseDate(dateStr)
    ddd = ddmm2ddd(mm, dd)
    return y4 * 1000 + ddd

dt = "4/2/2012"
print(getDayofYear(dt))


