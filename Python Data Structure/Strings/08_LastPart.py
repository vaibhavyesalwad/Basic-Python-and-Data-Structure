"""Program to get the last part of a string before a specified character"""
string = 'https://www.w3resource.com/python-exercises/string'
print(string.rsplit('-', 1)[0])    # rsplit starts splitting from end
print(string.rsplit('/', 1)[0])      # one split from end

