"""Program to reverse the order of the items in the array"""
import array as arr
numbers = arr.array('I', [5, 4, 3, 2, 1])       # Created array
numbers = numbers[::-1]         # reverse order assigned to given array
print(numbers)
