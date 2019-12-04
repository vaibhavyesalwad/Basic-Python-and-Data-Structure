"""Program to count the number of strings where the string length is 2 or more and the first
and last character are same from a given list of strings"""
data = ['abc', 'xyz', 'aba', '1221']
count = sum(True for d in data if len(d) >= 2 if d[0] == d[-1])  # use sum fn & nested loops in one line
print(f'{count} elements of data satisfy the condition')   # True is 1 for evaluation/ we can directly use 1
