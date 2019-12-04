"""Program to find the list of words that are longer than n from a given list of words"""
n = 6
words = ['Mumbai', 'Pune', 'Delhi', 'Chennai', 'Kolkata', 'Hyderabad', 'Ahmedabad', 'Bangalore', 'Indore']
print(f'words of length > 6: {[word for word in words if len(word) > 6]}')   # list comprehension
