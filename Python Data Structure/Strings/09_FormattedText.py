"""Program to display formatted text (width=50) as output"""
import textwrap
string = '''Python is a widely used high-level, general-purpose, interpreted,
   dynamic programming language. Its design philosophy emphasizes
   code readability, and its syntax allows programmers to express
   concepts in fewer lines of code than possible in languages such
   as C++ or Java'''
#print(textwrap.wrap(string, width=50))
print(textwrap.fill(string, width=50))       # print text in more than 50(width) columns

#help(textwrap)
