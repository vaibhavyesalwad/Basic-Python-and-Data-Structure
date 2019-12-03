"""Program to check multiple keys exists in a dictionary"""
dict1 = {'a': 1, 'b': 2, 'c': 3}
# using membership operator 'in' for iterables & in dictionary it checks keys
print(f'If z & b are present as keys: {all(key in dict1 for key in ("z", "b"))}')
# all() checks if all entries are True
print(f'If c & b are present as keys: {all(key in dict1 for key in ("c", "b"))}')
