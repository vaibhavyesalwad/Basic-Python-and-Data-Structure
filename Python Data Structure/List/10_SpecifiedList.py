"""Program to print a specified list after removing the 0th, 4th and 5th elements"""
data = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(f'Specified list:{[data[i] for i in range(len(data)) if i not in [0, 4, 5]]}')  # list comprehension
