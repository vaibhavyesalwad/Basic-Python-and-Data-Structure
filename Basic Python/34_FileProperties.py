"""Program to retrieve file properties"""
import os, time
print('05_PrintCalendar.py')          # file of which properties are to be displayed
print(f'Access time: {time.ctime(os.path.getatime("05_PrintCalendar.py"))}')
print(f'Modified time: {time.ctime(os.path.getmtime("05_PrintCalendar.py"))}')
print(f'Change time: {time.ctime(os.path.getctime("05_PrintCalendar.py"))}')
print(f'Size: {os.path.getsize("05_PrintCalendar.py")}')  # size of file
