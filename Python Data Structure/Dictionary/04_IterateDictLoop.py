"""Program to iterate over dictionaries using for loops"""
dict1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for key, value in dict1.items():  # iterate dict.items() in for loop it will give key & value
    print(key, value)

'''
for item in dict1.items():         # prints items in dictionary
    print(item)
'''

'''
for item in dict1:
    print(item)                # prints only keys
'''