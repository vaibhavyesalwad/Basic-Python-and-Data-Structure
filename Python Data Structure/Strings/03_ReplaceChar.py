"""program to get a string from a given string where all occurrences of its first char have been
changed to '$', except the first char itself"""
string = 'restart'
ch = 'r'
i = string.index(ch)                # using str.replace() method returns new string with all replacements
print(string[:i+1]+string[i+1:].replace(ch, '$'))
# count given replace that many characters only
