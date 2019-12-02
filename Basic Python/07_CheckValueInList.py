""" Program to check whether a specified value is contained in a group of values in Test Data"""


def check_value(number, sequence):
    """Checks whether given number is present in given list/sequence of numbers"""
    if number in sequence:
        return True
    return False


test_data = [1, 5, 8, 3]
print('test data:', test_data)
num = int(input('Enter number to check in test data:'))
print(check_value(num, test_data))         # prints returning value of function
