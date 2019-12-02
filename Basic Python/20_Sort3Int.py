"""Program to sort three integers without using conditional statements and loops"""
a, b, c = 3, 2, 1
print(a, b, c)
s = a + b + c               # get sum
a, c = min(a, b, c), max(a, b, c)  # assign min to 'a' & max to 'c'
b = s - (a + c)             # get remaining value from sum as 'b'
print(a, b, c)
