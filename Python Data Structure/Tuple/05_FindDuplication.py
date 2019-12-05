"""Program to find the repeated items of a tuple"""
tuple1 = ('a', 'c', 'd', 'a', 'b', 'e', 'z', 'x', 'm')
print(f'Repeated elements: {tuple(t for t in set(tuple1) if tuple1.count(t) > 1)}')  # finding repeated distinct items
