"""Program to print a dictionary in table format"""
dict1 = {'a': [1, 2, 3, 4], 'b': [2, 3, 4, 5], 'c': [3, 4, 5, 6], 'd': [4, 5, 6, 7]}
values = []
for key, value in dict1.items():           # getting values of dictionary
    print(key, end=' ')                      # printing keys
    values.append(value)
print()
for i in range(len(value)):
    for ch in values:
        print(ch[i], end=' ')                 # printing values in columns of it's key
    print()
