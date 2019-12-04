"""Program to clone or copy a list"""
numbers = [[10, 20], 20, 30, 40]
list1 = numbers.copy()       # returns shallow copy i.e. reference to nested elements will be linked to earlier list
print(numbers)
print(list1)

'''
import copy
list1 = copy.copy(numbers) # shallow copy
list1 = copy.deepcopy(numbers) # deep copy # no reference to earlier list
'''