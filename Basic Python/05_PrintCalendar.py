"""Program to print the calendar of a given month and year"""
import calendar
yy = int(input('Enter year:'))
mm = int(input('Enter month in number:'))
print(calendar.month(yy, mm))           # prints month
