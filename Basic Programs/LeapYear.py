"""Check whether input year is Leap year or not"""
year = input('Enter year:')
y = int(year)
if len(year) != 4:
    print('Invalid year')
elif y % 4 == 0:
    if y % 100 == 0 and y % 400 != 0:
        print('Not leap year')
    else:
        print('Leap Year')
else:
    print('Not leap year')

