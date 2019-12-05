"""Program to lowercase first n characters in a string."""
string = 'Navi Mumbai is financial capital of India'
n = 15
print(f'Lower cased first {n} characters: {string[:n].lower()+string[n:]}')
# lower cased only first 15 characters & kept remaining same as it is
