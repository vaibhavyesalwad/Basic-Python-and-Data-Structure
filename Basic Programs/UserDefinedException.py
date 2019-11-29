"""Define exception for presence of any character other than alphabets"""


class NonAlphaError(Exception):            # make class inheriting from Exception class
    pass


try:
    name = input('Enter name:')
    if not name.isalpha():                   # define condition for input string
        raise NonAlphaError
except NonAlphaError:
    print('Anything other than alphabets is not allowed')

