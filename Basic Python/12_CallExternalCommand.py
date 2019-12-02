"""Program to call an external command in Python"""
import os                       # Using os module
command = input('Enter command:')
os.system(command)                          # os.system runs single linux command


