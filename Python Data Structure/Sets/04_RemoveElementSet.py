"""Program to remove item(s) from set"""
myset = {1, 2, 3, 4, 5}
a = 4; myset.remove(4)
print(f'{a} removed from myset and now myset is {myset}')         # removes a from set if a is present else KeyError
print(f'{myset.pop()} removed randomly and now myset is {myset}')  # removes an element arbitrarily(empty set KeyError)

# another approach
'''
myset.discard(a)   # will remove a from set if a is present else nothing no error
'''