"""Program which accepts a sequence of comma-separated numbers from user and generate a list and
a tuple with those numbers"""

numbers = input('Enter sequence of numbers:')
numbers = numbers.split(',')            # gives list of characters separated by comma ','
t = tuple(numbers)          # making tuple out of list
print(numbers)
print(t)
