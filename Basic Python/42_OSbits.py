"""Program to determine if the python shell is executing in 32bit or 64bit mode on operating system"""
import sys, math
print(f'{math.log2(sys.maxsize) + 1} bits')
