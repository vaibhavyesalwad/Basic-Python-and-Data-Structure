"""1. Program which accepts user's first and last name and print them in reverse order with a space between them. """

name = input('Enter first name and last name:')
fname, lname = name.split()           # creating  string for output
full_name = lname + ' ' + fname
print(full_name)

