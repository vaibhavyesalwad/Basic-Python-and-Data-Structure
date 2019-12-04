"""Program to create a dictionary from a string"""
string = 'w3resource'
dict1 = {ch: string.count(ch) for ch in string}       # Used dictionary comprehension for creating dictionary
print(dict1)
