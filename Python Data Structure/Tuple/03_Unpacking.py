"""program to unpack a tuple in several variables"""
a, b, c = (4, 'hello', [1, 2, 3])       # unpacking of in several variables
print(a, b, c)

'''
x = (4, 'hello', [1, 2, 3])       # packing
(a, b, c) = x                  # unpacking
print(a, b, c)

a, _, c = x      # ignoring 2nd item   '_' holds 2nd item '_' used as variable name
print(a, c)
'''