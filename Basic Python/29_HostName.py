"""Program to get the name of the host on which the routine is running"""
import socket                           # using socket module
name = socket.gethostname()                         # gets host name
print(f'Host name: {name}')