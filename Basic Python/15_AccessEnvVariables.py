"""Program to access environment variables"""
import os                 # using os module
print(os.environ)                           # show env variables
os.environ['HOME'] = '/home/PycharmProjects'     # Changing env variable (not changed permanently)
print(os.environ)