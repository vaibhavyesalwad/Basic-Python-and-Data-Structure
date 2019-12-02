"""Program to create a histogram from a given list of integers"""


def hist(sequence):
    """Prints histogram for integer values in given list"""
    for n in sequence:
        print('*'*n)


numbers = [2, 4, 3, 6, 4, 10]
hist(numbers)
