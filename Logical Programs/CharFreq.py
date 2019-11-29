"""Find frequency of character in string & store in dictionary"""

string = input('Enter string:')

char_freq = {}
unique = set(string)         # Got unique characters
for ch in unique:
    count = 0
    for c in string:
        if c == ch:
            count += 1

    char_freq[ch] = count

print(char_freq)
