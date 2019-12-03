"""Program to extract single key-value pair of a dictionary in variables"""
dictionary = {1: 2}
(key, value), = dictionary.items()          # dict.items() gives items in list of tuple of (key, value) pairs
print(key, value)

# This is how it happens
'''
dictionary = {1: 2, 3:4}
[(a, b), (c, d)] = dictionary.items()
print(a, b, c, d)
'''