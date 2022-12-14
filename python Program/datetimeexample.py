import datetime
#datetime.datetime(Year_Number, Month_Number, Day_Number, Hours, Minutes, Seconds)
print(dir(datetime))
l=dir(datetime)
for a in range(len(l)):
    print(l[a])

dt=datetime
print('Maximum Year  = ', datetime.MAXYEAR)
print('Minimum Year  = ', datetime.MINYEAR)
dt = datetime.date.today()
print('Today\'s Date = ', dt)
today = datetime.date.today()
print('Today\'s Date = ', today)
print('Year from Today\'s Date = ', today.year)
print('Month from Today\'s Date = ', today.month)
print('Day from Today\'s Date = ', today.day)
dt = datetime.datetime.now()
print(dt)
print('Today\'s Date and Time = ', dt)
dt = datetime.datetime.now()
print('Date and time  = ', dt)
print('Current Date   = ', dt.date())
print('Current Time   = ', dt.time())
dt = datetime.datetime.now()
print('Date = ', dt)
print('Year from Date        = ', dt.year)
print('Month from Date       = ', dt.month)
print('Day from Date         = ', dt.day)
print('Hour from Date        = ', dt.hour)
print('Minute from Date      = ', dt.minute)
print('Second from Date      = ', dt.second)
print('Microsecond from Date = ', dt.microsecond)
print('Weekday Number from Date = ', dt.weekday())
time = datetime.datetime.now()
print('Current Time                  = ', time)
print('Hour from Current Time        = ', time.hour)
print('Minute from Current Time      = ', time.minute)
print('Second from Current Time      = ', time.second)
print('Microsecond from Current Time = ', time.microsecond)
print(datetime.datetime.now())
print(datetime.datetime.now().isoformat())
dt = datetime.date(2018, 1, 31)
print(dt)
print(dt.isoformat())
dt2 = datetime.datetime(2014, 12, 31, 22, 33, 44)
print('Date and Time  = ', dt2)
dt = datetime.datetime.now()
print('Today\'s Date   = ', dt)
print('Timestamp       = ', dt.timestamp())
dt = datetime.datetime.now()
print('Date and Time = ', dt)
date_replace = dt.replace(hour=2)
print('Date and Time = ', date_replace)
date_replace2 = dt.replace(minute=59)
print('Date and Time = ', date_replace2)
date_replace3 = dt.replace(second=4)
print('Date and Time = ', date_replace3)
date_replace4 = dt.replace(microsecond=7)
print('Date and Time = ', date_replace4)
print('isoweekday from Date = ', dt.isoweekday())
print('astimezone from Date = ', dt.astimezone())
dt = datetime.date(2018, 12, 31)

tm = datetime.time(23, 59, 58)

combine_dt = datetime.datetime.combine(dt, tm)

print('Date           = ', dt)
print('Time           = ', tm)
print('Date and Time  = ', combine_dt)

print('Year           = ', combine_dt.year)
print('Month          = ', combine_dt.month)
print('Day            = ', combine_dt.day)
print('Hour           = ', combine_dt.hour)
print('Minute         = ', combine_dt.minute)
print('Second         = ', combine_dt.second)
print('Microsecond    = ', combine_dt.microsecond)

print('Minimum Date         = ', datetime.date.min)
print('Maximum Date         = ', datetime.date.max)
print('Resolution           = ', datetime.date.resolution)

