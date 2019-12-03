"""Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)"""
n = int(input('Enter total number ot items in dictionary:'))  # total items in dictionary
dict1 = {x: x*x for x in range(1, n+1)}        # dictionary comprehension
print(dict1)

