"""Program to remove the first occurrence of a specified element from an array"""
import array as arr
numbers = arr.array('I', [5, 4, 3, 2, 1, 5, 3, 5, 2, 1])
num = int(input('Enter number to remove:'))             # taking input for removing specified element
numbers.remove(num)                                # removing specified element from it's first occurrence
print(f'{num} removed and now array is {numbers}')
