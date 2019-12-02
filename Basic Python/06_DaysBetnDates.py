"""Program to calculate number of days between two dates"""
import datetime as dt
d1 = dt.datetime(2019, 12, 2)
d2 = dt.datetime(2019, 7, 12)
print(d1 - d2)           # calculate diff in datetime.timedelta object
print(type(d1 - d2))