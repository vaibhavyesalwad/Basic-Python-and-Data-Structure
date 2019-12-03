"""Sort (ascending and descending) a dictionary by value"""
d = {'a': 26, 'b': 25, 'y': 2, 'z': 1}
# to access and map key value pairs dict.item gives list of tuples of key, value pairs
print(f'Ascending order by value {dict(sorted(d.items(),key=lambda x: x[1]))}')  # using second element of tuple
print(f'Descending order by value {dict(sorted(d.items(),key=lambda x: x[1], reverse= True))}')  # reverse parameter


