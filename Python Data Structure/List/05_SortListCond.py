"""Program to get a list, sorted in increasing order by the last element in each tuple from
a given list of non-empty tuples"""
data = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
data.sort(key=lambda x: x[1])        # using lambda fn that returns second element from given index
print(data)

'''
data = sorted(d,key=lamda x: x[1])   # sorted returns sorted list while list.sort changes list itself & returns nothing
'''