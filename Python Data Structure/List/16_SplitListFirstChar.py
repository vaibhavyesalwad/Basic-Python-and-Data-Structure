"""Program to split a list based on first character of word"""
word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
             'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

# first of all generate keys and then for each key set of words
dictionary = {word[0]: {word1 for word1 in word_list if word1[0] == word[0]} for word in word_list}
print(dictionary)