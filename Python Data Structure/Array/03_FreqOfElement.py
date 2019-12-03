"""Program to get the number of occurrences of a specified element in an array"""
import array as arr
numbers = arr.array('I', [5, 4, 3, 2, 1, 5, 3, 5, 2, 1])  # created an array
num = int(input('Enter number to find frequency:'))
print(f'{num} occurred {numbers.count(num)} times')   # using array.count(i) built-in fn for finding frequency of number

