"""Program to remove an item from a tuple"""
# Tuple is immutable data type cannot be changed once created
tuple1 = (1, 'abc', [1, 2, 3], 4.5)   # however we can edit mutable items in tuple but cannot delete them
tuple1[2].clear()
print(tuple1)   # we cannot add or remove from tuple so no no methods for addition or deletion
