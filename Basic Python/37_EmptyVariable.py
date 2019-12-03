"""Program to empty a variable without destroying it"""
n = 20
d = {"x": 200}
print(n, d)
print(type(n)(), type(d)())       # int() gives 0, dict() gives {}, list() gives [], tuple gives () -> empty variables
