"""Program to generate all permutations of a list in Python"""
import itertools                               # using itertools module
numbers = [10, 20, 30, 40, 50]                               # itertools.permutations gives object
print(f'All possible permutations:\n {list(itertools.permutations(numbers))}')

# we should give input in set of numbers i.e. unique as it considers positions as unique
'''
list(itertools.permutations(mylist, n)   # gives permutations of length n for elements of mylist 
list(itertools.combinations(mylist, n)   # gives combinations of length n for elements of mylist
'''