"""Program that accepts a comma separated sequence of words as input and prints the unique words in sorted form
(alphanumerically)"""
words = input('Enter words:').split(',')
print(sorted(set(words)))      # using set for unique words and sorted fn for alphanumeric order
