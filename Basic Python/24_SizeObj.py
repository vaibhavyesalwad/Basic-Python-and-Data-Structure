"""Program to get the size of an object in bytes"""
import sys                         # using sys module
a = 'Vaibhav'
print(f'Size of a: {type(a)} {sys.getsizeof(a)} bytes')      # sys.getsizeof gives size of object in memory
