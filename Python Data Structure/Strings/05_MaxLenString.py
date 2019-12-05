"""Write function that takes a list of words and returns the length of the longest one"""


def max_len(list1):
    return max(map(lambda x: len(x), words))      # used map fn & max fn
    # map fn returns map object max fn works on objects


words = ['Mumbai', 'Pune', 'Delhi', 'Chennai', 'Kolkata', 'Hyderabad', 'Ahmedabad', 'Bangalore', 'Indore']
print(f'Length of longest word in list: {max_len(words)}')

