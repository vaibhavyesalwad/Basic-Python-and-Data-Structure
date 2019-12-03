"""Program to create a dictionary from a string"""
string = 'w3resource'
dict1 = {}                             # created empty dictionary
for ch in string:
    dict1[ch] = string.count(ch)        # putting items to  dictionary

print(dict1)
