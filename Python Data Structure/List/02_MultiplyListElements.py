"""Program to multiplies all the items in a list"""


def product(sequence):
    """Function returns product of elements of given list"""
    if len(sequence) == 0:
        return 'Empty list'
    prod = 1
    for n in sequence:
        prod = prod*n
    return prod


numbers = [1, 2, 3, 4, 5]
print(f'Products of elements: {product(numbers)}')        # printing returned value returned by product fn
