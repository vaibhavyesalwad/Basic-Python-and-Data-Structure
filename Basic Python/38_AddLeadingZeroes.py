"""Program to add leading zeroes to a string"""
string = 'BridgeLabz'
print(string.rjust(15, '0'))              # str.rjust(wd,fc) method prints 15 places & string aligned to right
# blank places on left will be filled with given character

# another approach
'''
print(string.zfill(15))    # fills 0s at blank places on left
'''



