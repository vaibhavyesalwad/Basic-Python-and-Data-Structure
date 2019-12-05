""" Program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends
with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged"""


def manipulate(string):
    """Function checks if length of string is at least 3,  then appends 'ing' to string not ending with 'ing'
    and appends 'ly' if string ends with 'ing', if length less than 3 do nothing to string"""
    if len(string) > 2:
        if string.endswith('ing'):
            return string + 'ly'
        else:
            return string + 'ing'
    else:
        return string


string1 = input('Enter string:')
print(manipulate(string1))     # printing returning value
