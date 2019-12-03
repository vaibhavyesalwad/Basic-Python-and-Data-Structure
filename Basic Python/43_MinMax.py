"""Build a function to find the maximum and minimum numbers from a sequence of numbers"""


def min_max(sequence):
    """Function returns minimum & maximum from given list of numbers"""
    if len(sequence) == 0:
        return 'Empty list'
    min = max = sequence[0]                              # assigning first element as min & max
    for num in sequence:
        if num > max:
            max = num                                   # if num > max assigning max to num
        elif num < min:
            min = num                                   # if num < min assigning min to num
    return min, max


numbers = [23, 4, 56, 5, 45, 6, 23, 45, 6, 79, 45, 56]
#numbers =[1]
print(min_max(numbers))

