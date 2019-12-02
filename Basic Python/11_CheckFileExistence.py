"""Program to check whether a file exists"""
import os                                    # using os module
if os.path.exists('01_FirstLastName.py'):        # checks existence of given file
    print('exists')                             # alternatively os.path.isfile('filename')
else:
    print("doesn't exist")
