"""Check whether two words are anagrams are not"""


def anagram(w1, w2):
    """Function returns boolean value after checking anagram condition for two words"""
    for ch in w1:
        if ch not in w2 or w1.count(ch) != w2.count(ch):
            return False
    return True


word1 = input('Enter first word:')
word2 = input('Enter second word:')
print(anagram(word1, word2))
