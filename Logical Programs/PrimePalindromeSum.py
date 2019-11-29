"""Find prime numbers in given range & then palindromes out of it & then calculate digit sum"""


def isPrime(num):
    if num > 1:
        for i in range(2, num//2+1):
            if num % i == 0:
                return False
        else:
            return True
    else:
        False


def isNumPalindrome(num):
    tmp = num
    sum = 0

    while num > 0:
        remainder = num % 10
        sum = sum*10 + remainder
        num //= 10

    if tmp == sum:
        return True
    else:
        return False


def digitSum(num):
    sum = 0
    while num > 0:
        remainder = num % 10
        sum += remainder
        num //=10

    return sum


start = int(input('Enter starting number:'))
end = int(input('Enter ending number:'))
count = 0

primes = [num for num in range(start, end+1) if isPrime(num)]
palindromes = [num for num in primes if isNumPalindrome(num)]

print(primes)
print(palindromes)
for n in palindromes:
    print(f'{n,digitSum(n)}', end=' ')



