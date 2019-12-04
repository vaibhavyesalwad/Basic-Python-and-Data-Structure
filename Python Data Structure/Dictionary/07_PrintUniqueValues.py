"""Program to print all unique values in a dictionary"""
mylist = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
          {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]      # sample list of data

unique = {value for element in mylist for key, value in element.items()}    # used set comprehension
print(f'Unique values: {unique}')
