"""Remove an item from a set if it is present in the set"""
myset = {1, 2, 3, 4, 5}
a = 7; myset.discard(a)                     # discard  removes element if element present else do nothing
print(f'{a} removed from myset if present and now myset is {myset}')
a = 4; myset.discard(a)
print(f'{a} removed from myset if present and now myset is {myset}')
