"""Read from text file and convert it into string & count words"""

with open('mydoc','r') as f:            # r read file in text t  default mode & closes it
    string = f.read()                   # reads file until end of file

print(string)
words = string.split()
print(f'total words: {len(words)}')        # count total words
