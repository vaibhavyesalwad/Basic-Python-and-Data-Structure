"""Find intersection and union of given 2 sets of numbers"""
a = [1, 2, 3, 4, 5, 6]
b = [7, 8, 9, 4, 3, 0, 2, 6]
print(a)
print(b)

alength = len(a)
blength = len(b)

if alength >= blength:
    large = a
    small = b
else:
    large = b
    small = a

common = [num for num in small if num in large]     # Traverse through small size list for minimum iterations
print('Intersection:', common)

union = [num for num in large]
for num in small:
    if num not in union:
        union.append(num)

print('Union:', union)


