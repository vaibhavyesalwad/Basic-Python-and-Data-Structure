"""Program to count the values associated with key in a dictionary"""
mylist = [{'id': 1, 'success': True, 'name': 'Lary'},  {'id': 2, 'success': False, 'name': 'Rabi'},
           {'id': 3, 'success': True, 'name': 'Alex'}]
count = 0
for element in mylist:                          # traverse through list
     count += element['success']               # Adding value for success key as True is 1 & False is 0

print(f'{count} have success as True')
