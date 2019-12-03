"""Program to count number of items in a dictionary value that is a list"""
dict1 = {'a': [1, 2, 3, 4], 'b': [2, 3, 4, 5], 'c': 1, 'd': 'z', 'e': (1,)}
count = 0
for value in dict1.values():             # iterate through values of dictionary
    count += isinstance(value, list)        # if value is list added True i.e. 1 else False i.e. 0

print(f'{count} values are list')