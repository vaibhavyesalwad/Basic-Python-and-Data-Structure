""" Concatenate dictionaries to create a new one"""
dict1 = {1: 10, 2: 20}     # creating dictionaries
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

resultant = {}
resultant.update(dict1)     # concatenating dict1 to resultant
resultant.update(dict2)
resultant.update(dict3)
print(resultant)
