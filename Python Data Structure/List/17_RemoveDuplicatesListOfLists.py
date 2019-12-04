"""Program to remove duplicates from a list of lists"""
data = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
for d in data:
    if data.count(d) > 1:
        data.remove(d)

print(f'After removing duplicates: {data}')
