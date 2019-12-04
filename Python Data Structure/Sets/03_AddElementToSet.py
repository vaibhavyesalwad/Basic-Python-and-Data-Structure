"""To add member(s) in a set"""
myset = {1, 2, 3, 4, 5}
a = 6; myset.add(a)             # added single element
print(f'{a} added to myset and now myset is {myset}')
a = (7, 8, 9)
myset.update(a)               # added multiple elements from iterable list/tuple/set/dictionary(only keys added)
print(f'{a} added to myset and now myset is {myset}')
