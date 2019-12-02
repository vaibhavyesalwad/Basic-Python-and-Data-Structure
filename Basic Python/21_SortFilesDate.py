"""Program to sort files by date"""
import glob                 # using glob module & os module
import os

os.chdir('/home/admin1/PycharmProjects/Fellowship/Basic Programs')      # changed working directory
files = glob.glob("*.py")
files.sort(key=os.path.getmtime)        # sorted according to date
print("\n".join(files))   # to print on every other line
