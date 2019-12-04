"""Program to print a dictionary in table format"""
dict1 = {'a': [1, 2, 3, 4], 'b': [2, 3, 4, 5], 'c': [3, 4, 5, 6], 'd': [4, 5, 6, 7], 'e': [5, 6, 7, 8]}
values = [value for key, value in dict1.items()]      # used list comprehension
for d in dict1:
    print(d, end=' ')
for i in range(len(values[0])):                     # iterate till end of each value i.e. list
    print()
    for ch in values:
        print(ch[i], end=' ')                 # printing values in columns of it's key
