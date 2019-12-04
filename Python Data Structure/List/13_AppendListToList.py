""" Program to append a list to the second list"""
odd = [1, 3, 5, 7]
even = [2, 4, 6, 8]
odd = odd + even           # adds multiples elements at end of a list  Alternative odd.extend(even) do the same
print(f'After appending even at end of odd:{odd}')
