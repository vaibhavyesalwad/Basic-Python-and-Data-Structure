"""Program to generate all permutations of a list in Python"""
import itertools                               # using itertools module
numbers = [10, 20, 30, 40, 50]                               # itertools.permutations gives object
print(f'All possible permutations:\n {list(itertools.permutations(numbers))}')
