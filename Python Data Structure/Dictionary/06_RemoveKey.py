"""Program to remove a key from a dictionary"""
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key = 3                                 # dict.pop(key) removes item with key from dictionary & returns value for key
print(f'Item with {key} and value {dict1.pop(key)} removed and now dictionary is {dict1}')


# alternative way
'''
del dict1[key]       # removes item with key from dictionary
'''