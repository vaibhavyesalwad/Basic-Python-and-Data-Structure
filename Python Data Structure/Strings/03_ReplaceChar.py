"""program to get a string from a given string where all occurrences of its first char have been
changed to '$', except the first char itself"""
string = 'restart'
new = string.replace('r', '$')               # using str.replace() method returns new string with all replacements
print(new.replace('$', 'r', 1))                # if count given replace that many characters only
