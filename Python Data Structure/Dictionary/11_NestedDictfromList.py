"""Program to convert a list into a nested dictionary of keys"""
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    dict1 = dict.fromkeys([num])                # creating dictionary in each iteration
    if num == 1:
        my_dictionary = dict1                    # parent dictionary
    if num > 1:
        dict2[num-1] = dict1               # assigning new dictionary crated as value for dictionary in last iteration
    dict2 = dict1

print(my_dictionary)
