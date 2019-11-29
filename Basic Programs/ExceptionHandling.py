"""Implement exception handling, take integer as input and make sure it is greater than 0"""

try:                               # checks real time error
    num = int(input('Enter a number:'))                # if input other than integer then raises ValueError
    assert num > 0                         # if input is integer but not positive integer then raises AssertionError
except ValueError:
    print('Please enter integer value')                      # handling exception with output message
except AssertionError:
    print('Only integers greater than 0 are allowed')
else:
    print('No Error')                               # if no error then executed
finally:
    print('Exception handling is done')                # printed regardless of error

