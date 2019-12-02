"""Program to get execution time for a Python method"""
import time                                    # using time module


def fibo(n):
    """Function prints given number of terms of fibonacci series and returns time for computation"""
    start = time.time()                                 # start is seconds elapsed since 'epoch'(12 am, 1 Jan 1970)
    a = 0
    b = 1
    for i in range(n):                          # printing n  terms in fibonacci series
        print(a, end=' ')
        a, b = b, a+b
    end = time.time()                                   # end is time(in seconds) elapsed since 'epoch'
    return end - start                              # returning diff between two instances of time end & start

num = int(input('Enter number of terms to printed in fibonacci series:'))
print(f'\n Time taken by fibo function for {num} terms is {fibo(num)} seconds')


