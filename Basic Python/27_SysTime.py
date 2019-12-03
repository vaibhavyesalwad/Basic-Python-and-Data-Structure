"""Program to print system time"""
import datetime                        # using datetime module
time = datetime.datetime.now()                 # get current time object
print(f'Current time: {time.strftime("%H:%M:%S")}')      # print hours, minutes & seconds out of object
