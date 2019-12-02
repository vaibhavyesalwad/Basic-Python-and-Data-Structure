"""Program to get file creation and modification date/times"""
import os, time                         # using both os & time module
# os.path.getmtime gives timestamp for last modification
print("Last modified: %s" % time.ctime(os.path.getmtime("03_DisplayFirstLast.py")))
# os.path.getctime gives  timestamp for creation
print("Created: %s" % time.ctime(os.path.getctime("03_DisplayFirstLast.py")))
