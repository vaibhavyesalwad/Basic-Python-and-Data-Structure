"""Program to use of frozensets"""
a = frozenset((10, 11, 12, 13, 14))      # it is like set and created by putting iterable data types in frozenset fn
print(a)                                    # key difference is IMMUTABLE unlike set

dict1 = dict.fromkeys(a)
print(dict1)                      # frozenset is perfect for keys for dictionary as unique and immutable
# it possess all methods of sets except editing methods for the set

