"""Program to count number of items in a dictionary value that is a list"""
dict1 = {'a': [1, 2, 3, 4], 'b': [2, 3, 4, 5], 'c': 1, 'd': 'z', 'e': (1,)}
# if value is list added True i.e. 1 else False i.e. 0
count = sum(isinstance(value, list) for value in dict1.values())      # sum fn & generator expression
print(f'{count} values are list')
