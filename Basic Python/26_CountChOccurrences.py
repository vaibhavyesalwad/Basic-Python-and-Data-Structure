"""Program to count the number occurrence of a specific character in a string"""
string = 'BridgeLabz is a good place to work'
print(string)
ch = input("Enter character to find it's occurrences:")
print(f'{ch} occurred {string.count(ch)} times')                # string.count(ch) gives count of ch in string
