"""Find frequency of character in string & store in dictionary"""

string = input('Enter string:')

char_freq = {}
unique = []
for ch in string:
    count = 0
    if ch not in unique:
        unique.append(ch)
        for c in string:
            if c == ch:
                count += 1

        char_freq[ch] = count

print(char_freq)
