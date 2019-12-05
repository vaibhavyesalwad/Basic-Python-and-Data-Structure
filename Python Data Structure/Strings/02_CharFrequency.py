"""Program to count the number of characters (character frequency) in a string"""
string = 'google.com'
print(f"Frequency dictionary: {({ch: string.count(ch) for ch in string})}")        # used dictionary comprehension
