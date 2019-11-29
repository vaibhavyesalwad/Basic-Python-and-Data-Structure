"""Sort numbers in list using Selection sort algorithm"""
numbers = [int(n) for n in input('Enter list of numbers:').split()]
print(numbers)

for i in range(len(numbers)-1):             # find n-1 times minimum for n numbers
    min = i
    for j in range(i+1, len(numbers)):         # find minimum in each iteration
        if numbers[j] < numbers[min]:
             min = j

    numbers[i], numbers[min] = numbers[min], numbers[i]

print(numbers)