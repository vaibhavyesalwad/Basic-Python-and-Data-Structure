"""Check whether two words are anagrams are not"""


def count(ch, w):
    i = 0
    for j in w:
        if j == ch:
            i += 1
    return i


def anagram(w1, w2):
    for ch in w1:
        if ch not in w2 or count(ch, w1) != count(ch, w2):
            return False
    return True


word1 = input('Enter first word:')
word2 = input('Enter second word:')
print(anagram(word1, word2))
