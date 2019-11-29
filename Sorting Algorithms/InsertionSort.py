"""Sort numbers in list using Insertion sort algorithm"""
numbers = [int(i) for i in input('Enter list of numbers:').split()]
print(numbers)

for i in range(1, len(numbers)):            # first element already sorted
    j = i                                # insert element at j index in left part of array at it's appropriate position
    while j >= 1:
        if numbers[j] < numbers[j-1]:
            numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
        j -= 1

print(numbers)
