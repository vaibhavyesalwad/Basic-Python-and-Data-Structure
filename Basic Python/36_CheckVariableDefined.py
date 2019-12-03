"""Program to determine if variable is defined or not"""
#x = 4
try:                                        # using try and except block
    print(f'x defined and x = {x}')              # if variable is not defined interpreter raises NameError exception
except NameError:
    print('x not defined')              # exception handling by showing message
