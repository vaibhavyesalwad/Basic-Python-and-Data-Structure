"""Program to get an absolute file path"""
import os
print(os.getcwd())                       # Complete/absolute path for current file i.e. current working directory
os.chdir('/home/admin1/PycharmProjects/Fellowship')   # changed current working directory
print(os.path.abspath('File and Exception Handling/FileOperations.py'))   # got full/absolute path for FileOperations.py
