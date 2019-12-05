"""Program to create the clone of a tuple"""
import copy
t = (1, 'abc', [1, 2, 3], 4.5)    # created tuple
tuple1 = copy.copy(t)          # shallow copy of tuple- change reflected after change in nested elements of original
tuple2 = copy.deepcopy(t)          # deep copy of tuple- no change after change in nested elements of original tuple
print(tuple1)
print(tuple2)
