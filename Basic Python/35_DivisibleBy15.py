"""Program to get numbers divisible by fifteen from a list using an anonymous function"""
numbers = [10, 15, 20, 25, 30, 40, 52, 60]
multiples = list(filter(lambda x: x % 15 == 0, numbers))        # filter(fn,list) filter out unnecessary numbers
print(f'Multiples of 15: {multiples}')      # lambda is anonymous fn returns True if number is divisible by 15
