"""Program to print the documents (syntax, description etc.) of Python built-in function(s)"""
import builtins
func = input('Enter built-in function:')
attr = getattr(builtins, func)              # getting attribute of given object
print(attr.__doc__)                         # printing docstring for attribute

"""
help(func)              # another way 
"""