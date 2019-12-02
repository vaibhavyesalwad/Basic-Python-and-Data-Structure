"""Program to concatenate all elements in a list into a string and return it"""


def concat(sequence):
    """Function concatenates elements of given list into string and return string"""
    string = ''
    for ch in sequence:
        string += str(ch)
    return string

mylist = ['vaibhav', 'om', 'sanket']
print(concat(mylist))
