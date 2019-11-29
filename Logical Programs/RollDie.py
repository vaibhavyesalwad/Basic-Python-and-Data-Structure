"""Find number that has occurred maximum times and it's frequency"""
import random

n = int(input('Enter number of times you want to roll a die:'))

result = [random.randint(1, 6) for i in range(n)]
print(result)

max_count = 0
counts = []

for i in range(1, 7):               # Any number would be in range(1,7) for randint(1,6)
    count = 0
    for k in result:
        if k == i:
            count += 1
    counts.append(count)            # counts frequency of each character & find max frequency
    if count > max_count:
        max_count = count

for j in range(1, 7):
    if counts[j-1] == max_count:
        print(j, end=' ')

print(f'occurred maximum {max_count} times')


