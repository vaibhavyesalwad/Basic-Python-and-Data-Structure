"""Program to remove duplicates from a list of lists"""
data = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
data1 = []
for d in data:
    if d not in data1:
        data1.append(d)
print(f'After removing duplicates: {data1}')
