"""Program to print all unique values in a dictionary"""
mylist = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
          {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]      # sample list of data

unique = set()
for element in mylist:                         # iterate in given list
    for key, value in element.items():
        unique.add(value)                               # taking out only values from dictionaries

print(f'Unique values: {unique}')
